# 八维视觉自评的原始提示词

用户于 2026-10-24 提供，原作者和发布链接未提供。此页用于查阅历史。

```text
::OBJECTIVE{site_design|pri:OVERRIDE_ALL}
  target: build page to award-tier visual standard
  ACCEPT: no visible improvement remaining across all CHECK dimensions
  BENCHMARK: Awwwards | Webby Awards | FWA winning entries

::CHECK{typography|standard:award_tier}
::CHECK{whitespace|standard:award_tier}
::CHECK{visual_hierarchy|standard:award_tier}
::CHECK{color|standard:award_tier}
::CHECK{motion|standard:award_tier}
::CHECK{micro_interaction|standard:award_tier}
::CHECK{responsive|standard:award_tier}
::CHECK{originality|standard:award_tier}

::LOOP{self_review|trigger:on_completion}
  [READ] current page against CHECK list
  [COMPARE] each dimension to BENCHMARK entries
  [IF] gap found => [PATCH] then re-enter LOOP
  [IF] no gap => [Ω]
```
