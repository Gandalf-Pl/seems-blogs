# My Jekyll Blog

一个基于 Jekyll + Chirpy 主题的个人博客，部署在 GitHub Pages。

## ✨ 特性

- 🌙 **暗黑模式** - 默认暗黑主题，护眼舒适
- 🔍 **内置搜索** - 快速找到想要的内容
- 📱 **响应式设计** - 完美适配手机、平板、桌面
- 🏷️ **标签分类** - 文章归类清晰
- 📊 **代码高亮** - 优雅的代码展示
- 📑 **文章目录** - 长文阅读更轻松

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/my-blog.git
cd my-blog
```

### 2. 安装依赖

```bash
bundle install
```

### 3. 本地预览

```bash
bundle exec jekyll serve
```

访问 http://localhost:4000

### 4. 部署到 GitHub Pages

1. 在 GitHub 创建同名仓库 `yourusername.github.io`
2. 推送代码到 main 分支
3. 在仓库 Settings → Pages 中启用 GitHub Pages
4. 等待几分钟，访问 https://yourusername.github.io

## 📝 写作

在 `_posts` 目录下创建新文章：

```bash
# 文件名格式: YYYY-MM-DD-title.md
# 例如: 2026-02-27-my-new-post.md
```

文章头部格式：

```markdown
---
title: "文章标题"
date: 2026-02-27 12:00:00 +0800
categories: [技术]
tags: [javascript, react]
---

文章内容...
```

## 🎨 自定义

编辑 `_config.yml` 修改站点配置：

- `title` - 站点标题
- `description` - 站点描述
- `author` - 作者信息
- `url` - 站点地址
- `theme_mode` - 主题模式 (light/dark)

## 📄 许可证

本博客使用 [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) 主题，遵循 MIT 许可证。
# Force rebuild
