# YouTube Watcher

抓取并阅读 YouTube 视频字幕，助您快速总结视频内容、解答疑问或提取关键信息。

## 功能

### 1. 字幕抓取
- 自动下载视频字幕
- 支持自动生成的字幕
- 多语言字幕支持
- 时间戳保留

### 2. 内容分析
- 视频内容总结
- 关键信息提取
- 问答交互
- 章节划分

### 3. 批量处理
- 播放列表处理
- 频道视频分析
- 批量转录

## 使用

```bash
# 获取视频字幕
youtube-watcher subtitles "https://youtube.com/watch?v=xxx"

# 总结视频内容
youtube-watcher summarize "https://youtube.com/watch?v=xxx" --length short

# 提取特定信息
youtube-watcher extract "https://youtube.com/watch?v=xxx" --query "关键数据"

# 下载字幕文件
youtube-watcher download "https://youtube.com/watch?v=xxx" --format srt

# 分析播放列表
youtube-watcher playlist "https://youtube.com/playlist?list=xxx" --summarize

# 问答模式
youtube-watcher ask "https://youtube.com/watch?v=xxx" --question "视频讲了什么？"
```

## 输出格式

```markdown
# 视频标题

## 摘要
简要概述视频内容...

## 关键点
- 要点 1
- 要点 2
- 要点 3

## 详细内容
[00:00] 开场介绍
[01:30] 第一部分内容
[05:45] 核心观点阐述
...

## 时间戳
- 00:00 - 简介
- 02:15 - 主题开始
- 10:30 - 案例分析
```

## 使用场景

- 快速了解长视频内容
- 提取教程中的关键步骤
- 研究竞争对手视频
- 学习外语听力材料
- 内容创作灵感收集

## 依赖

- youtube-transcript-api
- yt-dlp (可选，用于下载)
