"""Validate toolkit links and resource records."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import date
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
FIELDS = [
    "name", "url", "category", "description_zh", "source", "source_post_url",
    "verified_at", "pricing", "license",
]
LINK = re.compile(r"!?\[[^\]\n]*\]\((?:<([^>]+)>|([^\s)]+))\)")


def check_link(value, source, errors, external):
    url = urlsplit(value)
    if url.scheme in ("http", "https") and url.netloc:
        external.add(url._replace(fragment="").geturl())
    elif not url.scheme and not url.netloc:
        target = (source.parent / unquote(url.path)).resolve() if url.path else source
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f"{source.relative_to(ROOT)}: broken link {value}")
        elif url.fragment and target.suffix == ".md":
            headings = re.findall(r"^#{1,6}\s+(.+)$", target.read_text(), re.M)
            slugs = {
                re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
                for heading in headings
            }
            fragment = unquote(url.fragment)
            if fragment not in slugs:
                errors.append(f"{source.relative_to(ROOT)}: missing anchor {value}")


def check_csv(errors, external):
    path = ROOT / "resources.csv"
    seen = {}
    with path.open(encoding="utf-8", newline="") as file:
        reader = csv.reader(file, strict=True)
        if next(reader, None) != FIELDS:
            errors.append("resources.csv: unexpected header or UTF-8 BOM")
        for values in reader:
            line = reader.line_num
            if len(values) != len(FIELDS):
                errors.append(f"resources.csv:{line}: expected {len(FIELDS)} columns")
                continue
            row = dict(zip(FIELDS, values))
            for field in ("url", "source_post_url"):
                if row[field]:
                    check_link(row[field], path, errors, external)
                else:
                    errors.append(f"resources.csv:{line}: missing {field}")
            url = urlsplit(row["url"])
            key = (url.netloc.lower().removeprefix("www."), url.path.rstrip("/"), url.query)
            if key in seen:
                errors.append(f"resources.csv:{line}: duplicate URL on line {seen[key]}")
            seen[key] = line
            if row["verified_at"]:
                try:
                    if date.fromisoformat(row["verified_at"]).isoformat() != row["verified_at"]:
                        raise ValueError
                except ValueError:
                    errors.append(f"resources.csv:{line}: expected YYYY-MM-DD")
    if not seen:
        errors.append("resources.csv: no resource rows")
    return len(seen)


def check_external(url):
    request = Request(url, headers={"User-Agent": "UI-Design-Toolkit-Link-Check"})
    try:
        with urlopen(request, timeout=8):
            return None
    except HTTPError as error:
        status = "broken" if error.code in (404, 410) else "unverified"
        return status, f"HTTP {error.code}", url
    except (URLError, TimeoutError, OSError) as error:
        return "unverified", str(error), url


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external", action="store_true", help="probe external links")
    args = parser.parse_args()
    errors = []
    external = set()
    count = check_csv(errors, external)
    markdown = [
        *ROOT.glob("*.md"),
        *(ROOT / "references").rglob("*.md"),
        *(ROOT / "examples").rglob("*.md"),
        *(ROOT / "archive").rglob("*.md"),
    ]
    for path in markdown:
        content = re.sub(r"^```.*?^\s*```\s*$", "", path.read_text(), flags=re.M | re.S)
        for angled, plain in LINK.findall(content):
            check_link(angled or plain, path, errors, external)
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked {len(markdown)} Markdown files and {count} CSV rows")
    if args.external:
        with ThreadPoolExecutor(max_workers=12) as pool:
            results = [result for result in pool.map(check_external, sorted(external)) if result]
        for status, reason, url in results:
            print(f"{status}: {reason} {url}")
        print(f"Probed {len(external)} URLs, {len(results)} need review")
        return int(any(status == "broken" for status, _, _ in results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
