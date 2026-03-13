# OpenAI Whisper

本地语音转文本服务，通过 Whisper CLI 实现高质量离线语音识别。

## 特点

- 🎤 **离线识别** - 无需网络连接，本地处理
- 🔑 **无需 API 密钥** - 完全免费使用
- 🌍 **多语言支持** - 支持 99 种语言
- ⚡ **高质量** - 接近人类水平的识别准确率

## 安装

```bash
# 安装 whisper
pip install openai-whisper

# 或安装 faster-whisper（更快）
pip install faster-whisper
```

## 使用

```bash
# 基本转录
whisper audio.mp3

# 指定语言
whisper audio.mp3 --language Chinese

# 输出不同格式
whisper audio.mp3 --output-format srt
whisper audio.mp3 --output-format vtt
whisper audio.mp3 --output-format txt

# 翻译为英文
whisper audio.mp3 --task translate

# 指定模型（tiny/base/small/medium/large）
whisper audio.mp3 --model medium
```

## 模型选择

| 模型 | 大小 | 速度 | 准确率 |
|------|------|------|--------|
| tiny | 39 MB | 最快 | 一般 |
| base | 74 MB | 快 | 良好 |
| small | 244 MB | 中等 | 较好 |
| medium | 769 MB | 较慢 | 好 |
| large | 1550 MB | 最慢 | 最好 |

## Python API

```python
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## 应用场景

- 会议录音转录
- 视频字幕生成
- 语音笔记整理
- 播客内容提取
