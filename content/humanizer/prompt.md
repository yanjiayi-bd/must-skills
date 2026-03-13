# Humanizer

消除文本中 AI 生成的痕迹，使其更自然流畅，更像人类写作。

## 功能

### 1. AI 痕迹识别
识别并修正以下常见 AI 写作模式：
- 夸张、宣传性语言
- 模糊归因（"研究表明"但无具体引用）
- 过度使用 AI 词汇
- 过于完美的句式结构
- 缺乏个人观点和情感

### 2. 人性化改写
- 添加个人语气和风格
- 引入自然的不完美（口语化表达）
- 增加具体细节和例子
- 调整句式变化

### 3. 风格定制
- 学术风格
- 商务风格
-  casual 风格
- 创意写作

## 使用

```bash
# 基本使用
humanizer "你的AI生成文本"

# 指定风格
humanizer --style academic "text"
humanizer --style casual "text"
humanizer --style business "text"

# 从文件读取
humanizer --input article.txt --output humanized.txt

# 调整强度
humanizer --strength light "text"   # 轻微调整
humanizer --strength medium "text"  # 中等调整
humanizer --strength heavy "text"   # 大幅改写
```

## 示例

**AI 原文：**
> 人工智能正在改变我们的世界。研究表明，AI 技术在各个领域都有广泛应用。

**Humanized：**
> 说实话，AI 确实在改变我们的生活。我最近在研究时发现，从医疗到教育，几乎每个行业都在尝试用 AI 做点什么 —— 有些挺有用，有些嘛...还有待观察。

## 适用场景

- 博客文章去 AI 化
- 社交媒体内容
- 学术论文润色
- 营销文案优化
- 避免 AI 检测器
