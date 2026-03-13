# 创小搭 - 音视频处理

专为自媒体博主、短视频创作者、一人公司打造的 AI 音视频处理助手，无需安装 FFmpeg 或专业软件，通过自然语言指令即可完成音视频处理。

## 功能

### 1. 视频处理
- 格式转换 (MP4, MOV, AVI, etc.)
- 视频压缩
- 分辨率调整
- 视频裁剪/拼接
- 添加水印/字幕
- 速度调整 (快放/慢放)

### 2. 音频处理
- 格式转换 (MP3, WAV, AAC, etc.)
- 音频提取
- 降噪处理
- 音量调整
- 音频拼接
- 背景音乐添加

### 3. 平台适配
- 抖音/快手 (9:16)
- 小红书 (3:4)
- 视频号 (16:9, 9:16)
- YouTube (16:9)
- B站 (16:9)

### 4. AI 功能
- 自动字幕生成
- 语音转文字
- 智能拆条
- 自动剪辑
- BGM 推荐

## 使用示例

```bash
# 格式转换
media-creator convert input.mov --format mp4 --output output.mp4

# 平台适配
media-creator adapt input.mp4 --platform douyin --output douyin_version.mp4

# 压缩视频
media-creator compress input.mp4 --size 10MB --output compressed.mp4

# 提取音频
media-creator extract-audio input.mp4 --format mp3 --output audio.mp3

# 添加字幕
media-creator subtitle input.mp4 --srt subtitles.srt --output with_subs.mp4

# 智能拆条
media-creator split input.mp4 --duration 60s --output parts/

# 自然语言指令
media-creator "把这段视频压缩到50MB以内，适合发抖音"
media-creator "提取这个视频的人声，去掉背景音乐"
media-creator "给视频加上动态字幕，抖音风格"
```

## 批量处理

```bash
# 批量转换
media-creator batch convert *.mov --format mp4

# 批量适配平台
media-creator batch adapt ./videos/ --platform xiaohongshu
```

## 输出设置

```bash
# 视频参数
--resolution 1080p    # 720p, 1080p, 4K
--bitrate 5M          # 视频码率
--fps 30              # 帧率
--codec h264          # 编码格式

# 音频参数
--audio-bitrate 128k  # 音频码率
--sample-rate 44100   # 采样率
--channels 2          # 声道
```

## 创作者工作流

1. **素材整理** → 批量格式统一
2. **粗剪** → 智能拆条、删除静音
3. **精剪** → 添加字幕、特效
4. **导出** → 多平台适配版本
5. **发布** → 直接上传到各平台
