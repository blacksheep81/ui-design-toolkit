# UI Design Toolkit

[中文](README.md)

A UI design skill for AI coding assistants (Claude Code, Codex, and other tools that support `SKILL.md`). It gives the assistant a five-step design workflow, a set of design principles, and task-specific references that are loaded only when needed.

The skill content is written in Chinese. Assistants can follow it regardless of the language you prompt in, and several references (Chinese typography, Chinese-specific "AI look" signals) target Chinese-language interfaces in particular.

## Install

```sh
npx skills add blacksheep81/ui-design-toolkit
```

Or copy this repository into your assistant's skills directory. The entry point is `SKILL.md`; reference files live in `references/`.

## Use

- "Use ui-design-toolkit to build an order management page."
- "Use ui-design-toolkit to review this UI and list concrete problems."
- "Improve the mobile information hierarchy using this brand and the existing components."

Workflow: understand the brief → find references → define the design system → implement → render and review. Existing components and tokens are reused first; user requirements and product context override any default in the skill.

## What's inside

| File | Purpose |
| --- | --- |
| SKILL.md | Entry point, scope, and completion criteria |
| references/toolkit-workflow.md | The five-step workflow and pre-delivery review |
| references/principles.md | 20 UI design principles, summarized as actionable rules |
| references/page-patterns.md | Structure and pitfalls per page mode: landing, admin/dashboard, docs, showcase |
| references/anti-slop.md | Checklist for avoiding the generic "AI template" look |
| references/design-md-template.md | DESIGN.md and token template, Tailwind v4 mapping, font pairing |
| references/accessibility-states-motion.md | WCAG contrast, focus, loading/empty/error states, motion, responsive rules |
| references/dark-mode.md | Semantic token mapping, elevation, implementation, and checks for dark themes |
| references/chinese-typography.md | Chinese font stacks, weight fallback, line height, punctuation, mixed-script spacing |
| references/data-visualization.md | Chart selection, axes, palettes, stat cards, chart states |
| references/mobile-native.md | iOS / Android platform conventions, layout, navigation, accessibility |
| references/i18n.md | Text expansion, translatable copy, date/number formats, RTL |
| references/review-template.md | Fixed output format and severity levels for UI reviews |
| references/visual-self-review.md | Eight-dimension visual self-review with a bounded fix loop |
| references/liquid-glass.md | Liquid-glass material tiers, parameters, and checks |
| references/claude-design-system.md | A flat, claude.ai-style design spec (compiled from screenshots; not official Anthropic documentation) |
| references/agent-usage.md | Usage loop for Claude Code / Codex, shadcn/ui and Tailwind v4 conventions |
| references/community-methods.md | Community methods and what was actually verified |
| references/design-resources.md, references/toolkit-resource-directory.md, references/himanshu-resource-map.md | Curated design reference sites and tools |
| resources.csv | 112 resource records with source fields |
| examples/DESIGN.example.md | A filled-in DESIGN.md for a fictional order management admin |
| examples/review-example.md | A sample review written with the review template (fictional page) |
| SOURCES.md | Sources, verification scope, and attribution |

The resource lists are a reference index. Nothing is installed automatically, some entries are unverified, and counts, prices, and licenses may have changed.

## Sources and usage rights

See [SOURCES.md](SOURCES.md). This repository does not include the Refactoring UI book, third-party site assets, or third-party skill source code. Linking to a resource does not mean its content may be freely copied; no unified license has been applied to this collection, so redistribution rights for the resource files and for the text in this repository need to be confirmed separately.
