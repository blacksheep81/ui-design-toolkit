# 在 Claude Code、Codex 中使用与组件库约定

## 安装位置

- Claude Code：`~/.claude/skills/ui-design-toolkit/`（个人）或项目内 `.claude/skills/ui-design-toolkit/`。
- Codex：`~/.codex/skills/ui-design-toolkit/`；也可用 `npx skills add blacksheep81/ui-design-toolkit` 安装到支持的助手。
- 安装或更新后开启新会话，让助手重新加载 skill。

## 推荐循环

1. 读项目：`DESIGN.md`、`PRODUCT.md`、Tailwind 配置或 `@theme`、`components/ui`。缺 DESIGN.md 时按 design-md-template.md 先写一版并请用户确认方向。
2. 计划：列出页面区块、所用组件、状态与断点，再写代码。
3. 实现：一次只改一个区块（首屏 → 主要内容 → 表单/卡片），每块完成后渲染。
4. 截图评审：用 Playwright 或浏览器 MCP 截桌面与移动端，按 visual-self-review.md 与 accessibility-states-motion.md 检查，限次修正。
5. 汇报：说明改了哪些文件、验证了哪些尺寸与状态、剩余问题。

Claude Code 可用 `/` 命令或直接说“使用 ui-design-toolkit”触发；Codex 中直接点名 skill。没有浏览器能力时，明确说明未做视觉验证。

## 组件库：shadcn/ui 与 Tailwind v4

- 已用 shadcn/ui 时优先复用 `components/ui` 中的组件，用 CLI 添加缺失组件，不手写同名替代品；样式差异通过主题变量和 `variant` 调整，避免到处覆盖 className。
- shadcn 官方提供面向 AI 助手的 skills 文档（见 SOURCES.md），可让助手了解组件、注册表与 CLI 用法。
- Tailwind v4 用 CSS 中的 `@theme` 定义 token，不再依赖 `tailwind.config.js`；新增颜色、字体、间距先加 token，再使用工具类，禁止散落的任意值（如 `text-[#7c3aed]`）。
- 图标库保持一种；图标尺寸和描边与文字字号对齐。
- 引入新依赖前确认项目框架、React 版本与许可证。

## 与其他设计 skill 并用

本 skill 负责流程、原则与资源路由。需要更强的命令式精修（如 bolder、quieter、audit）可另装 Impeccable；需要特定风格可参考 Taste Skill 或 awesome-design-md 中的品牌 DESIGN.md。多个 skill 冲突时，用户需求与项目 DESIGN.md 优先。
