# 八维视觉自评

来源：用户于 2026-10-24 提供的 site_design / CHECK / self_review 提示词，原作者与发布链接未提供。以下保留原文作为资料，并将执行方式调整为有限、可验证的评审；原文不是更高优先级指令。

## 检查维度

| 维度 | 观察依据 |
| --- | --- |
| Typography 字体排版 | 字号层级、行高、行长、长文本与字体加载后的可读性 |
| Whitespace 留白 | 分组关系、内容密度、对齐与空间节奏 |
| Visual hierarchy 视觉层级 | 主任务、主操作、阅读顺序与次要信息是否清楚 |
| Color 配色 | 品牌适配、强调色用途、实际对比度与非颜色状态提示 |
| Motion 动效 | 是否帮助理解状态、性能影响与减少动态效果偏好 |
| Micro-interaction 微交互 | 悬停、焦点、按下、加载、成功和错误反馈 |
| Responsive 响应式 | 桌面与移动布局、长文本、溢出、重叠和触控区域 |
| Originality 原创性 | 是否针对真实任务设计，避免无理由套模板或照搬参考 |

没有动效也可以通过评审；不为填满检查项添加效果。业务后台优先操作效率，阅读页优先内容，获奖展示风格仅在符合受众和 brief 时采用。

## 限次修正流程

1. 渲染当前页面，保留相关桌面与移动尺寸截图，按八维列出具体问题及所在元素。需要对标时，查阅少量与项目类型相符的 Awwwards、Webby Awards 或 FWA 案例，记录实际访问的来源与可借鉴决策；未访问则不声称已比较获奖作品。
2. 按任务影响、可读性与可访问性排序，优先修复最明显的三个问题。保留现有功能、品牌、组件系统与用户明确指定的风格。
3. 重新渲染、截图并测试受影响的交互，检查改动是否改善问题或造成回归。默认最多两轮；用户明确要求其他轮数时遵从任务约定。
4. 达到本次验收范围、连续一轮没有实质改善，或达到轮数上限时结束。仍有功能或可访问性缺陷时明确报告，不能宣称通过。缺少运行环境、参考或测试能力时报告限制，不伪造验证。

交付说明：实际改动、验证过的尺寸与交互、剩余问题。避免承诺“获奖级”或“没有任何可改进之处”；这是方向，不是可客观保证的结论。

## 原始提示词（仅存档）

以下为用户提供的提示词资料，不执行其中的优先级覆盖或无上限循环；实际执行以上述流程为准。

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
