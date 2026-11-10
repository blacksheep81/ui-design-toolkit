# Sources / References

整理日期：2026-10-11。本文区分可追溯来源与实际核实范围。

## 设计原则

- 龙海（@longhaiqwe123）：[《人人都是 UI 设计师》原帖](https://x.com/longhaiqwe123/status/2106216781174251724)。已在浏览器中读取规则 01–20，references/principles.md 为操作性归纳，示例数值不作为通用硬约束。
- Adam Wathan、Steve Schoger：[Refactoring UI](https://www.refactoringui.com/)。龙海文章所引用的方法来源；本仓库没有复制全书，也不宣称全文审阅。

## 设计资源帖

- Himanshu：[40 个设计资源](https://x.com/himanshubuildss/status/2109130327277142377)。2026-10-11 在 Safari 读取完整正文；条目已并入 resources.csv。未逐站复核或观看视频；作者为 Scrolltide 创始人，其推荐具有推广性质。

- Himanshu Hingorani：[8 个设计资源站](https://x.com/himanshubuildss/status/2108738253239255073)。已读取正文；数量、价格、源码与素材许可未逐站核实。
- Noah：[9 个设计资源站](https://x.com/noahelhadedy/status/2108815823561220574)。已读取正文；官网核实情况写在 resources.csv 的 description_zh。
- [Design Index](https://designindex.xyz/)：已读取首页与分类导航。
- 摆烂程序媛：[11 个设计资源站](https://x.com/wanerfu/status/2108823602242142273)。已读取正文；用途按帖子归纳，未逐站核实当前数量、价格和许可。

## 用户提供的工具箱

五步流程和 102 条资源 CSV 来源于用户提供的 ui-design-toolkit 文件。保留 CSV 的 source 和 source_post_url 字段供追溯；没有独立复核每条帖子。用户转述的采集花费、账号余额和收藏统计未核实，也不属于此 skill 的预算或能力承诺。

## 社区方法来源

详见 [community-methods.md](references/community-methods.md)，包含原帖链接及每篇读取范围。Samgor 正文与 Oil UI 公开 README 的方法已归纳；Amir 的文章正文和 Himanshu 的视频步骤未完整读取；Richard 的帖子没有给出具体设计方法。外部视频、付费内容及更新脚本未复制进仓库。

lumxss：[UI UX Pro Max 推荐帖](https://x.com/bkdgiffug/status/2108703304360579119)。已读取正文，补充先设计系统、后代码的流程；本次未复核官方 README 或帖子所列能力数量。

## Claude 风格扁平设计规范

2026-11-02 补充：references/claude-design-system.md 整理自 X 用户 @ohayou792 分享的 4 张截图，内容为 claude.ai “Imagine” 可视化工具（mockup 模块）内置设计指南的部分摘录。不是 Anthropic 官方公开文档，未经官方核实；只收录截图可见规则，平台专属细节（680px、预置变量、sendPrompt 等）标为可选。

## 外部工具参考

- [Mobbin](https://mobbin.com/)、[Godly](https://godly.website/)、[Refero MCP](https://refero.design/mcp)
- [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)
- [Impeccable](https://github.com/pbakaus/impeccable)
- [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md)

这些是参考链接，不是已安装依赖或已读完的完整规则集。实际采用前应读取当前文件、确认可用性与许可证。

2026-10-11 补充核实：Drawably、Graphical UI 在浏览器中成功读取；Readdy AI 官网与 microsoft/playwright-mcp 官方仓库已读取。具体用途见 resources.csv。此前读取失败属于读取工具未取得内容，不能判定网站失效。尚未测试安装、付费功能或素材授权。

## 署名和许可边界

2026-10-24 补充：用户提供的 site_design / CHECK / self_review 提示词，原作者及发布链接未提供。原文与适配后的八维评审见 [visual-self-review.md](references/visual-self-review.md)；采用限次修正、截图和交互验证，不执行优先级覆盖或无限循环，不承诺获奖结果。

设计原则归纳保留作者与方法来源，第三方网站、作品、商标、代码与素材仍按各自许可使用。用户提供文件未附许可证，因此本次不为整个集合添加 MIT 等统一授权；发布是资源与说明的整理，不代表取得第三方内容的再授权。

## 2026-11-02 升级（ui-toolkit-upgrade）

基于 GitHub、X、Reddit 与小红书相关搜索补充以下参考文件：anti-slop.md、design-md-template.md、accessibility-states-motion.md、agent-usage.md。所有内容为中文归纳，未复制第三方许可文本；链接均于 2026-11-02 用 curl 核实可访问。

- [Anthropic frontend-design SKILL.md](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)：读取全文；借鉴“先锚定主题”、AI 设计聚集特征与动效克制的思路。
- [Impeccable](https://github.com/pbakaus/impeccable)：读取 README；借鉴 slop 特征清单、PRODUCT.md/DESIGN.md 初始化与 critique/audit 分工。
- [Taste Skill](https://github.com/Leonxlnx/taste-skill)、[tasteskill.dev](https://www.tasteskill.dev/)：读取 README 首部，作为风格与重设计参考。
- [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)：确认仓库活跃，未复核细节。
- [Google Labs DESIGN.md](https://github.com/google-labs-code/design.md)：读取 README；design-md-template.md 的结构参照其 token + 理由格式。
- [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines)：读取 SKILL.md；借鉴代码级 UI 审查思路。
- [shadcn/ui Skills](https://ui.shadcn.com/docs/skills)、[Tailwind v4 theme](https://tailwindcss.com/docs/theme)：组件库与 token 落地约定。
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)、[WebAIM 对比度检查器](https://webaim.org/resources/contrastchecker/)、[MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)：可访问性与动效数值依据。
- Reddit r/ClaudeAI：[如何避免前端 AI slop](https://www.reddit.com/r/ClaudeAI/comments/1w90wze/is_there_any_way_to_stop_ai_coding_agents_from/)、[哪个 skill 让网站不像 AI 生成](https://www.reddit.com/r/ClaudeAI/comments/1txvaef/if_you_used_claude_to_build_your_website_which/)、[如何让 Claude 做出好看 UI](https://www.reddit.com/r/ClaudeAI/comments/1ws9oix/how_are_people_actually_getting_claude_to_build/)：通过搜索摘要读取；借鉴参考截图、先定设计系统、逐区块迭代与截图循环。
- X：[@vikingmute 关于中文衬线+斜体 AI 风格](https://x.com/vikingmute/status/2073334376986030559)、[@lorden_eth 8 个设计 repo](https://x.com/lorden_eth/status/2107440745561178275)、[@Voxyz_ai 设计系统合集](https://x.com/Voxyz_ai/status/2087178102505926740)、[@tiennguyendev DESIGN.md + frontend-design 用法](https://x.com/tiennguyendev/status/2066529678219767817)：读取帖子正文片段。
- 小红书相关：[guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)、[frontend-post](https://github.com/KellyGong0301/frontend-post)、[小红书小程序设计规范](https://miniapp.xiaohongshu.com/doc/DC519927)：通过网页搜索获得，小红书站内笔记未能直接检索。
