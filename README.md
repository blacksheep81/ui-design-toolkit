# UI Design Toolkit

面向 AI 编程助手的 UI 设计 skill：统一使用 `ui-design-toolkit` 入口，包含五步设计流程、20 条 UI 原则、反 AI 模板味清单、DESIGN.md 模板、可访问性与状态规范、Claude Code/Codex 使用说明、Claude 风格扁平设计规范、液态玻璃、八维视觉自评、资源索引及社区方法。

## 安装

```sh
npx skills add blacksheep81/ui-design-toolkit
```

也可将本仓库下载到支持 SKILL.md 的助手技能目录。核心入口为 SKILL.md，引用文件在 references/ 中。

## 使用

- “使用 ui-design-toolkit 做一个订单管理页面。”
- “使用 ui-design-toolkit 评审这个 UI，列出具体问题。”
- “根据这个品牌和现有组件，改善移动端信息层级。”

流程：读需求 → 找参考 → 定设计系统 → 实现 → 渲染与交互评审。已有项目优先复用组件和 token，具体规则服从用户需求及产品场景。

## 内容

| 文件 | 用途 |
| --- | --- |
| SKILL.md | 技能入口、适用范围和完成标准 |
| references/toolkit-workflow.md | 五步流程与交付评审 |
| references/principles.md | 20 条设计原则的原创操作归纳 |
| references/community-methods.md | 社区来源、设计系统先行、多方向探索与克制设计，含待核实媒体标记 |
| references/design-resources.md | 动效参考的选择、实现和验收 |
| references/claude-design-system.md | claude.ai 风格扁平设计规范（截图整理，非官方文档；平台细节可选） |
| references/anti-slop.md | 反 AI 模板味清单（含中文界面信号） |
| references/design-md-template.md | DESIGN.md 与 token 模板、Tailwind v4 映射、字体搭配 |
| references/accessibility-states-motion.md | WCAG 对比度、焦点、加载/空/错误状态、动效与响应式 |
| [references/visual-self-review.md](references/visual-self-review.md) | 八维视觉自评与限次修正 |
| [references/liquid-glass.md](references/liquid-glass.md) | 液态玻璃类型、参数与实现取舍 |
| references/agent-usage.md | Claude Code / Codex 使用循环与 shadcn、Tailwind v4 约定 |
| resources.csv | 166 条资源，含来源、核实日期、价格和许可 |
| references/toolkit-resource-directory.md | 按问题检索 CSV 的入口 |
| references/himanshu-resource-map.md | Himanshu 资源帖的兼容入口 |
| [SOURCES.md](SOURCES.md) | 来源、核实范围与署名 |
| [CHANGELOG.md](CHANGELOG.md) | 按日期查更新 |

资源列表属于参考索引；不会自动安装其他 skills、付费服务或素材。部分条目待核实，资源数量、价格和许可可能变化。

[八维视觉自评](references/visual-self-review.md)：覆盖排版、留白、层级、配色、动效、微交互、响应式与原创性，默认最多两轮修正，以截图和交互验证结果，并保留用户提供的原始提示词。

## 来源与使用权

原创归纳文字采用 [CC BY 4.0](LICENSE)。第三方内容的署名和许可见 [SOURCES.md](SOURCES.md)。

## 校验

运行 `python3 scripts/check_resources.py` 检查文档内链和 CSV。加 `--external` 可检查外链。GitHub Actions 在推送、PR 和每周任务中运行相应检查。
