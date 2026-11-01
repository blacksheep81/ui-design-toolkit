# Claude 风格扁平设计规范（claude.ai Imagine 工具指南）

适用：做 claude.ai 风格的内嵌组件（widget）、卡片、表单、看板、SVG 图表，或需要扁平、紧凑、极简且兼容暗色模式的界面。用户品牌规范与现有设计系统优先。

> **来源说明：** 整理自 X 用户 @ohayou792 分享的 4 张截图，内容是 claude.ai “Imagine — Visual Creation Suite” 可视化工具（mockup 模块）内置 `read_me` 指南的部分摘录。**不是 Anthropic 官方公开文档**，未经官方核实；只收录截图中可见的规则，原文未详细涉及动效与无障碍，不据此补写规则。
>
> **平台专属细节可选：** 680px 容器宽度、预置 CSS 变量名（`--surface-*`、`--pad-*` 等）、SVG 预置类（`t`/`ts`/`th`、`c-blue` 等）、预置表单样式以及 `sendPrompt` 等宿主交互，只在 claude.ai 环境内成立；其他项目按自身 token 和视口映射，不必照抄。

## 理念

- **无缝**：组件看起来像宿主页面的一部分，用户察觉不到边界。
- **扁平**：不用渐变、网格/噪点背景和装饰效果；除功能性焦点环外不用阴影。（与[原则 19](principles.md) 的“阴影也应克制”一致，本规范更严格。）
- **紧凑**：只在组件里展示要点，其余放进正文说明。
- **文字在外，视觉在内**：标题、介绍、总结写在普通回复文本里；HTML/SVG 只承载视觉内容。

## 代码顺序（流式输出）

HTML 按 简短 `<style>` → 内容 HTML → `<script>` 放最后，让有用内容尽早出现。

## 布局与间距

- 容器 680px（平台专属）；响应式列 `grid-template-columns: repeat(auto-fit, minmax(160px, 1fr))`。
- 留白充足（见[原则 7、9](principles.md)）。Token：`--pad-{sm,md,lg,xl}`、`--gap-{xs,sm,md,lg,xl}`。

## 字体与文字色

- `--font-sans`、`--font-voice`（衬线）、`--font-mono`。
- 文字色三档：`--text-primary`、`--text-secondary`（弱化）、`--text-muted`（提示）；角色色 `--text-{accent,danger,success,warning}`。层级思路见[原则 3](principles.md)。
- SVG 中每个 `<text>` 都要带类（`t`、`ts`、`th`）；不要省略 fill，也不要用 `fill="inherit"`。

## 颜色与表面

- 表面：`--surface-2`（白）、`--surface-1`（卡片）、`--surface-0`（页面底）；角色底色 `--bg-{accent,danger,success,warning}`（浅底深字思路见[原则 14](principles.md)）。
- **暗色模式必须支持**：所有颜色在亮/暗两种模式下都可用。HTML 一律用 CSS 变量，不写死颜色；SVG 用预置颜色类，不写 `<style>` 颜色块。
- 图表最多 2 条色阶。颜色表达含义（状态、等级）时加一行图例；否则用单一中性色阶（多线索表达见[原则 15](principles.md)）。

## 边框、圆角与组件

- 边框统一 `0.5px solid var(--border)`；悬停/强调用 `--border-strong`，更强 `--border-stronger`；角色边框 `--border-{accent,danger,success,warning}`。
- 圆角：多数元素 `var(--radius)`（8px）；卡片 12px；更大圆角直接写 12px/16px。
- 卡片：`var(--surface-2)` 背景、0.5px 边框、12px 圆角、内边距 `1rem 1.25rem`。
- 表单元素（input、select、textarea、button、range）在平台内已预置样式，直接写裸标签；文本输入框高 36px，滑块轨道 4px、拇指 18px。

## 状态

悬停 → `--border-strong`。焦点环是唯一允许的阴影。状态用角色 token（danger/success/warning/accent）。

## 图表复杂度上限（硬性）

- 方框副标题 ≤5 个词，细节放点击展开或正文。
- 一行横向最多 4 个方框（满宽约 140px/个）；5 个以上则缩到 ≤110px、折成两行，或拆成总览 + 详情。

## 反模式

- 渐变、阴影、发光、纹理、装饰效果。
- 在组件内放段落、标题和大段说明。
- 写死颜色、暗色模式下失效的颜色、SVG 中的 `<style>` 颜色块。
- 粗边框、超过 2 条色阶、无图例的含义色、过于拥挤的图表行。
