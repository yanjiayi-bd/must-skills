# Must-Skills for OpenClaw

精选 OpenClaw 高价值技能集合，复刻自 ClawHub Top 10 热门技能，涵盖飞书生态、系统运维、多媒体处理等领域。

## 📊 技能概览

### 技能矩阵

| 技能 | 分类 | 版本 | 描述 |
|------|------|------|------|
| `feishu-doc` | 飞书集成 | 1.0.0 | 飞书云文档协作与管理 |
| `feishu-drive` | 飞书集成 | 1.0.0 | 飞书云盘文件操作 |
| `feishu-wiki` | 飞书集成 | 1.0.0 | 飞书知识库管理 |
| `feishu-perm` | 飞书集成 | 1.0.0 | 飞书权限与安全控制 |
| `healthcheck` | 系统运维 | 1.0.0 | 系统健康检查与诊断 |
| `1password` | 系统运维 | 1.0.0 | 1Password 凭证管理 |
| `nano-banana-pro` | 多媒体 | 1.0.0 | Gemini 图像生成专业版 |
| `video-frames` | 多媒体 | 1.0.0 | FFmpeg 视频转图片 |
| `skill-creator` | 基础工具 | 1.0.0 | 技能创建与打包工具 |
| `weather` | 基础工具 | 1.0.0 | 实时天气查询与预报 |

## 📁 目录结构

```
must-skills/
├── README.md              # 本文件
├── feishu-doc/            # 飞书文档协作
│   ├── skill.json
│   └── prompt.md
├── feishu-drive/          # 飞书云盘
│   ├── skill.json
│   └── prompt.md
├── feishu-wiki/           # 飞书知识库
│   ├── skill.json
│   └── prompt.md
├── feishu-perm/           # 飞书权限管理
│   ├── skill.json
│   └── prompt.md
├── healthcheck/           # 系统健康检查
│   ├── skill.json
│   └── prompt.md
├── 1password/             # 1Password 集成
│   ├── skill.json
│   └── prompt.md
├── nano-banana-pro/       # AI 图像生成
│   ├── skill.json
│   └── prompt.md
├── video-frames/          # 视频处理
│   ├── skill.json
│   └── prompt.md
├── skill-creator/         # 技能创建器
│   ├── skill.json
│   └── prompt.md
└── weather/               # 天气查询
    ├── skill.json
    └── prompt.md
```

## 🚀 快速开始

### 安装技能

```bash
# 安装单个技能
cp -r must-skills/feishu-doc ~/.openclaw/skills/

# 或使用 openclaw CLI
openclaw skills install ./must-skills/feishu-doc

# 安装所有技能
for skill in must-skills/*/; do
  openclaw skills install "$skill"
done
```

### 使用技能

```bash
# 查看已安装技能
openclaw skills list

# 运行技能
openclaw skills run weather --input location="北京"
openclaw skills run feishu-doc --input action="list"
openclaw skills run healthcheck --input target="all"
```

## 📖 使用场景

### 1. 飞书生态集成

**适合人群**: 使用飞书的企业团队、飞书管理员

```bash
# 场景：团队需要快速迁移文档
openclaw skills run feishu-doc --input action="export" --input folder="项目文档"

# 场景：设置部门权限
openclaw skills run feishu-perm --input action="grant" --input user="team@company.com" --input scope="editor"
```

### 2. 系统运维监控

**适合人群**: DevOps 工程师、系统管理员

```bash
# 场景：服务器健康检查
openclaw skills run healthcheck --input target="all" --input notify=true

# 场景：批量获取服务器凭证
openclaw skills run 1password --input action="get" --input item="prod-db-credentials"
```

### 3. 多媒体处理

**适合人群**: 内容创作者、视频编辑

```bash
# 场景：生成配图
openclaw skills run nano-banana-pro --input prompt="科技感办公场景，蓝色调，极简风格"

# 场景：提取视频封面帧
openclaw skills run video-frames --input video="demo.mp4" --input interval="00:00:01"
```

### 4. 日常工具

**适合人群**: 所有用户

```bash
# 场景：出门前查天气
openclaw skills run weather --input location="上海" --input days=3

# 场景：快速创建新技能
openclaw skills run skill-creator --input skill_name="my-custom-skill"
```

## 🔧 技能配置

### Feishu 集成

需要在 `openclaw.json` 中配置飞书凭证：

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "cli_xxxxx",
      "appSecret": "your-secret"
    }
  }
}
```

### 1Password 集成

需要配置 1Password CLI 认证：

```bash
op account add --address my.1password.com --email user@example.com
```

### Gemini API

设置 API 密钥：

```bash
export GEMINI_API_KEY="your-api-key"
```

## 📚 技能文档

| 技能 | 文档 | 示例 |
|------|------|------|
| feishu-doc | [README](feishu-doc/README.md) | [examples](feishu-doc/examples/) |
| healthcheck | [README](healthcheck/README.md) | [examples](healthcheck/examples/) |
| weather | [README](weather/README.md) | [examples](weather/examples/) |

## 🏆 技能对比

| 特性 | ClawHub 原版 | 本复刻版 |
|------|-------------|---------|
| 开源协议 | 闭源 | MIT |
| 可定制性 | 有限 | 完全可定制 |
| 本地运行 | ❌ | ✅ |
| 离线支持 | ❌ | ✅ |
| 二次开发 | 受限 | 完全开放 |

## 🤝 贡献

欢迎贡献新的技能！请遵循以下规范：

1. 每个技能独立目录
2. 包含 `skill.json` 和 `prompt.md`
3. 添加使用示例
4. 更新本 README

```bash
# 提交新技能
git checkout -b feature/my-skill
git add must-skills/my-skill/
git commit -m "feat: add my-skill"
git push origin feature/my-skill
```

## 📄 许可证

MIT License - 详见 [LICENSE](../LICENSE)

## 🙏 致谢

技能设计参考：
- [ClawHub](https://clawhub.ai) - 技能榜单与灵感
- [Awesome OpenClaw Skills](https://github.com/VoltAgent/awesome-openclaw-skills) - 社区技能资源

---

**维护者**: yanjiayi-bd  
**最后更新**: 2025-01
