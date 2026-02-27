from PIL import Image, ImageDraw, ImageFont
import os

# 创建画布 - 模拟网页预览
width, height = 1200, 1600
img = Image.new('RGB', (width, height), '#1a1a2e')
draw = ImageDraw.Draw(img)

# 尝试加载字体，如果没有就用默认
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    font_tag = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
except:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_tag = ImageFont.load_default()

# 绘制导航栏背景
draw.rectangle([0, 0, width, 70], fill='#16162a')
draw.line([0, 70, width, 70], fill='#2a2a4a', width=1)

# Logo - 渐变效果模拟
draw.text((40, 20), "我的博客", fill='#a78bfa', font=font_title)

# 导航链接
nav_items = ["首页", "归档", "分类", "标签", "关于"]
x_pos = 700
for item in nav_items:
    color = '#ffffff' if item == "首页" else '#9ca3af'
    draw.text((x_pos, 25), item, fill=color, font=font_text)
    x_pos += 90

# 主内容区起始位置
content_y = 120

# 搜索框
draw.rounded_rectangle([40, content_y, width-40, content_y+50], radius=8, fill='#252542', outline='#3a3a5c')
draw.text((60, content_y+15), "🔍 搜索文章...", fill='#6b7280', font=font_text)
content_y += 80

# 分类标签
categories = ["全部", "技术", "随笔", "生活", "读书笔记"]
x_cat = 40
for cat in categories:
    if cat == "全部":
        # 激活状态 - 渐变背景
        draw.rounded_rectangle([x_cat, content_y, x_cat+70, content_y+35], radius=20, fill='#7c3aed')
        draw.text((x_cat+18, content_y+8), cat, fill='#ffffff', font=font_small)
    else:
        draw.rounded_rectangle([x_cat, content_y, x_cat+70, content_y+35], radius=20, fill='#252542')
        draw.text((x_cat+18, content_y+8), cat, fill='#9ca3af', font=font_small)
    x_cat += 85
content_y += 70

# 文章卡片 1
card1_y = content_y
draw.rounded_rectangle([40, card1_y, width-40, card1_y+200], radius=12, fill='#252542', outline='#3a3a5c')
# 标题
draw.text((60, card1_y+20), "🎉 欢迎使用我的 Jekyll 博客", fill='#ffffff', font=font_title)
# 元信息
draw.text((60, card1_y+60), "📅 2026-02-27    ⏱️ 3 分钟阅读    👁️ 128 次阅读", fill='#6b7280', font=font_small)
# 摘要
draw.text((60, card1_y+95), "这是我的第一篇博客文章！基于 Jekyll + Chirpy 主题构建，", fill='#a1a1aa', font=font_text)
draw.text((60, card1_y+120), "支持暗黑模式、实时搜索、代码高亮等特性...", fill='#a1a1aa', font=font_text)
# 标签
tags1 = ["jekyll", "github-pages", "博客"]
x_tag = 60
for tag in tags1:
    draw.rounded_rectangle([x_tag, card1_y+160, x_tag+80, card1_y+185], radius=15, fill='#4c1d9520')
    draw.text((x_tag+10, card1_y+163), tag, fill='#a78bfa', font=font_tag)
    x_tag += 95

content_y += 230

# 文章卡片 2
card2_y = content_y
draw.rounded_rectangle([40, card2_y, width-40, card2_y+200], radius=12, fill='#252542', outline='#3a3a5c')
draw.text((60, card2_y+20), "深入理解 React Hooks 原理", fill='#ffffff', font=font_title)
draw.text((60, card2_y+60), "📅 2026-02-25    ⏱️ 8 分钟阅读    👁️ 256 次阅读", fill='#6b7280', font=font_small)
draw.text((60, card2_y+95), "React Hooks 是 React 16.8 引入的新特性，它让我们", fill='#a1a1aa', font=font_text)
draw.text((60, card2_y+120), "在函数组件中使用状态和其他 React 特性...", fill='#a1a1aa', font=font_text)
tags2 = ["react", "javascript", "前端"]
x_tag = 60
for tag in tags2:
    draw.rounded_rectangle([x_tag, card2_y+160, x_tag+80, card2_y+185], radius=15, fill='#4c1d9520')
    draw.text((x_tag+10, card2_y+163), tag, fill='#a78bfa', font=font_tag)
    x_tag += 95

content_y += 230

# 文章卡片 3
card3_y = content_y
draw.rounded_rectangle([40, card3_y, width-40, card3_y+200], radius=12, fill='#252542', outline='#3a3a5c')
draw.text((60, card3_y+20), "Docker 容器化部署实战指南", fill='#ffffff', font=font_title)
draw.text((60, card3_y+60), "📅 2026-02-20    ⏱️ 12 分钟阅读    👁️ 512 次阅读", fill='#6b7280', font=font_small)
draw.text((60, card3_y+95), "从 Dockerfile 编写到多阶段构建，从单机部署到", fill='#a1a1aa', font=font_text)
draw.text((60, card3_y+120), "Kubernetes 集群，带你掌握容器化部署...", fill='#a1a1aa', font=font_text)
tags3 = ["docker", "kubernetes", "devops"]
x_tag = 60
for tag in tags3:
    draw.rounded_rectangle([x_tag, card3_y+160, x_tag+80, card3_y+185], radius=15, fill='#4c1d9520')
    draw.text((x_tag+5, card3_y+163), tag, fill='#a78bfa', font=font_tag)
    x_tag += 95

# 右侧悬浮按钮
btn_x = width - 90
draw.rounded_rectangle([btn_x, 400, btn_x+50, 400+50], radius=8, fill='#252542')
draw.text((btn_x+15, 415), "🔍", font=font_text)
draw.rounded_rectangle([btn_x, 460, btn_x+50, 460+50], radius=8, fill='#252542')
draw.text((btn_x+15, 475), "🌙", font=font_text)
draw.rounded_rectangle([btn_x, 520, btn_x+50, 520+50], radius=8, fill='#252542')
draw.text((btn_x+15, 535), "⬆️", font=font_text)

# 页脚
footer_y = height - 80
draw.line([40, footer_y, width-40, footer_y], fill='#3a3a5c', width=1)
draw.text((450, footer_y+30), "© 2026 我的博客 · Powered by Jekyll & Chirpy", fill='#6b7280', font=font_small)

# 保存图片
output_path = '/root/.openclaw/workspace/my-blog/preview.png'
img.save(output_path, 'PNG')
print(f"Preview saved to: {output_path}")
