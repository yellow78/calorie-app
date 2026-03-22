---
title: Food Calorie Analyzer
emoji: 🍱
colorFrom: green
colorTo: yellow
sdk: gradio
sdk_version: 5.0.0
app_file: app.py
pinned: false
---

# 食物熱量分析器

上傳一張食物照片，AI 將為你估算熱量。

## 使用方式

1. 上傳食物照片
2. 點擊「分析熱量」
3. 查看每樣食物的估計熱量

## 環境變數設定

在 Huggingface Spaces 的 Settings > Variables and secrets 中設定：

- `GOOGLE_API_KEY`：你的 Google Gemini API Key
