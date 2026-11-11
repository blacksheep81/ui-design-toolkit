---
name: ui-design-toolkit
description: Design, implement, and review web or app UI and components, or choose design references and resources. Use for UI 设计工具箱、ui-design-toolkit、页面设计、界面精修、UI 评审、落地页、后台与仪表盘、表单与表格、图表、DESIGN.md、暗色模式、中文排版、移动端 App、多语言界面、液态玻璃和去 AI 模板味.
---
# UI 设计工具箱

做出贴合需求、主次清晰且可验证的界面。用户指定的风格、品牌规范和现有设计系统优先；原则中的数值是起点，按语言、字体、内容密度与实际视口调整。

## 工作流

设计或实现界面时读取 [五步设计流程](references/toolkit-workflow.md)，依次理解需求、选参考、定设计系统、实现并验证。局部精修保留原有识别度，按问题修改；只评审时直接检查相关元素与状态。

- 明确页面主要任务、受众及模式：Persuade（营销行动）、Operate（操作效率）、Read（阅读理解）、Experience（作品展示）。已有项目先读 PRODUCT.md、DESIGN.md、组件与 token；只有分歧会实质改变结果时才澄清。
- 确定模式后读取 [按页面模式的结构与检查](references/page-patterns.md) 的对应小节：落地页与定价页、后台表格/筛选/表单/仪表盘、文档长文、作品展示。
- 制定或复用颜色、字体、间距与响应式约定。使用真实内容或明确标注的示例数据；按钮说明动作，错误提供恢复路径，空状态提供下一步。
- 需要处理层级、留白、排版、颜色、按钮、图片或空状态时，读取 [20 条 UI 设计原则](references/principles.md)。新设计先用灰度检查骨架；评审逐项处理适用的问题，保留有根据的例外。
- 做 claude.ai 风格内嵌组件、卡片、图表，或需要扁平、极简、兼容暗色模式的界面时，在定设计系统阶段读取 [Claude 风格扁平设计规范](references/claude-design-system.md)；680px 容器、预置变量和 sendPrompt 等平台专属细节可选。该文件整理自 claude.ai 工具指南截图，非 Anthropic 官方文档。
- 交付实现时渲染并检查相关桌面、移动尺寸、长文本、主要交互、键盘焦点、状态与实际对比度；有暗色模式时一起检查。动效支持减少动态效果偏好。交付建议时说明具体元素、改法与理由。
- 没有指定视觉方向时，读取 [反 AI 模板味清单](references/anti-slop.md)，先锚定主题并给出 2–3 个方向，避免紫色渐变、千篇一律卡片、中文衬线斜体大标题等默认值。
- 项目缺少设计规范时，按 [DESIGN.md 模板](references/design-md-template.md) 写出 token 与理由，并映射到 Tailwind v4 `@theme` 或 CSS 变量；含字体搭配速查。填写方式参考 [DESIGN.md 示例](examples/DESIGN.example.md)。
- 实现与评审时按 [可访问性、状态、动效与响应式](references/accessibility-states-motion.md) 检查对比度、焦点、加载/空/错误状态、减少动态效果与移动端规则。
- 需要亮、暗两套主题时，读取 [暗色模式](references/dark-mode.md)，用语义 token 映射并分别实测对比度。
- 界面以中文为主或中英混排时，读取 [中文界面排版](references/chinese-typography.md)：字体栈与字重回落、行高行长、标点和中英间距。
- 包含图表、指标卡或仪表盘时，读取 [数据可视化](references/data-visualization.md) 选图并确定色板、坐标轴与状态。
- 做 iOS、Android 原生 App 时，读取 [移动端原生 App 界面](references/mobile-native.md)，先遵守平台导航、触控目标与安全区习惯。
- 需要支持多语言或地区时，读取 [国际化与多语言界面](references/i18n.md)：文本膨胀、日期数字格式与 RTL。
- 在 Claude Code、Codex 中安装、按区块迭代与截图验证，或使用 shadcn/ui、Tailwind v4 时，读取 [助手使用与组件库约定](references/agent-usage.md)。
- 只评审或需要书面结论时，按 [UI 评审输出模板](references/review-template.md) 输出：范围、结论、带严重度的问题表（元素、问题、改法、依据）、保留项与待确认；写法参考 [评审示例](examples/review-example.md)。
- 交付前按 [八维视觉自评](references/visual-self-review.md) 检查适用维度；用户要求获奖级、视觉精修或自我迭代时，执行其中的限次修正流程。

## 按需选择参考

提炼参考中的层级、密度、导航、控件、响应式与状态决策，并适配当前项目。按任务选择少量来源，无需每次遍历所有清单。

- 常用网站、产品流程、组件、字体、图标与工具：读取 [工具箱资源目录](references/toolkit-resource-directory.md)，或检索 [分类资源 CSV](resources.csv)。
- 液态玻璃、磨砂玻璃或玻璃控件精修：读取 [液态玻璃类型与参数](references/liquid-glass.md)，按背景、可读性与性能选择材质。
- 导航、页脚、CTA、首屏、玻璃效果、动效和截图展示：读取 [补充设计参考站](references/design-resources.md)。定价、3D 或细分组件资源可继续读取其链接的分类索引。
- 缺少设计规范、探索多方案或优化业务界面的视觉克制程度：读取 [社区方法与核实范围](references/community-methods.md)。

采用资源时核实当前功能、框架兼容性和素材许可；工具与 MCP 按实际可用能力选择，列入资源表不代表已经配置。

## 完成标准

主任务与主操作可辨识；组内间距小于组间；文字与内容宽度适合实际视口；辅助文字可读；状态有颜色之外的表达；图像、图标和截图在展示尺寸下清晰；空状态提供可执行的下一步。处理适用的实质问题，报告实际验证范围和剩余限制。

## 内容来源

以用户的 UI Design Toolkit 五步流程、资源目录和 resources.csv 为基础，合并原 Longhai skill 的 20 条设计原则、社区方法和补充资源。来源与历史核实范围保留在对应参考文件中；本 skill 统一使用 ui-design-toolkit 名称。
