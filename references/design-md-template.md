# DESIGN.md 与设计 token 模板

用途：项目缺少设计规范时，在“定设计系统”阶段生成或补全仓库根目录的 `DESIGN.md`，之后每次改 UI 先读它。格式参考 Google Labs 的 DESIGN.md 规范：YAML front matter 放机器可读 token，Markdown 正文写使用理由。已有 token、Tailwind 主题或组件库时，从代码中提取，不另起一套。

## 模板

```md
---
name: <项目名>
colors:
  bg: "#FFFFFF"
  surface: "#F6F7F9"
  text: "#16181D"
  text-muted: "#5B6170"   # 在 bg 上对比度 ≥ 4.5:1
  border: "#E3E6EB"
  primary: "<品牌主色>"
  primary-contrast: "#FFFFFF"
  danger: "#C62828"
typography:
  font-sans: "<正文字体>, PingFang SC, Microsoft YaHei, sans-serif"
  font-display: "<标题字体，可与正文相同>"
  scale: [12, 14, 16, 20, 24, 32, 40]   # px
  line-height: { body: 1.6, heading: 1.25 }
spacing: [4, 8, 12, 16, 24, 32, 48, 64]
radius: { sm: 4px, md: 8px, lg: 12px, full: 9999px }
shadow: { sm: "0 1px 2px rgb(0 0 0 / .06)" }
motion: { fast: 120ms, base: 200ms, easing: "cubic-bezier(.2,.8,.2,1)" }
breakpoints: { sm: 640px, md: 768px, lg: 1024px, xl: 1280px }
---

## 概述
一句话视觉定位 + 页面模式（Persuade / Operate / Read / Experience）。

## 颜色
每个 token 的用途；强调色只用于哪些交互；暗色模式映射。

## 字体
字体选择理由、字号层级对应的元素、中英混排规则。

## 组件
按钮层级、表单、卡片、表格、弹层的约定；圆角与阴影如何对应层级。

## 状态
空、加载、错误、成功、禁用的统一写法。

## 禁止
本项目不使用的默认值（参见 anti-slop.md），例如“不用紫色渐变”“不用全大写标签”。
```

## 落地

- Tailwind v4：在 CSS 中用 `@theme { --color-primary: …; --font-sans: …; }` 定义同名变量，使 token 直接生成工具类；shadcn/ui 主题变量（`--background`、`--primary` 等）与上表一一映射。
- 纯 CSS：写入 `:root` 自定义属性，暗色模式在 `[data-theme="dark"]` 或 `prefers-color-scheme` 中覆盖。
- 修改 token 时同步更新 DESIGN.md 正文的理由，避免文档与代码漂移。

## 字体搭配速查

- 一个家族多字重通常足够；两个家族时，让标题与正文在结构上明显不同（如几何无衬线 + 人文衬线），避免两个相似无衬线。
- 正文行长控制在约 45–80 个拉丁字符或 25–40 个汉字；衬线正文行高略大于无衬线。
- 可从 Google Fonts、Fontshare 等免费来源选择，并确认中文字体的授权与文件体积。

来源：Google Labs DESIGN.md 规范、VoltAgent awesome-design-md、Tailwind CSS v4 主题文档；见 SOURCES.md。
