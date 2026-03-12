# Must-Skills for OpenClaw

精选 OpenClaw 高价值技能集合，按功能分类组织，包含 **ClawHub Top 10 热门技能复刻**。

## 🔥 ClawHub Top 10 热门技能

> 复刻自 [ClawHub](https://clawhub.ai) 官方热门榜单，按下载量排序

| 排名 | 技能 | 分类 | 描述 | 作者来源 |
|-----|------|------|------|---------|
| 1 | **gog** | productivity | Google Workspace 命令行工具 (Gmail/日历/云端硬盘/通讯录/表格/文档) | Peter Steinberger |
| 2 | **self-improving-agent** | core | 记录学习心得、错误与修正，推动持续改进 | pskoett |
| 3 | **tavily-search** | productivity | 通过 Tavily API 实现 AI 优化的网络搜索，精准无广告 | arun-8687 |
| 4 | **ontology** | core | 为结构化智能体记忆与可组合技能构建的类型化知识图谱 | oswalpalash |
| 5 | **find-skills** | core | 帮助用户发现并安装 skills 的元技能 | JimLiuxinghai |
| 6 | **summarize** | productivity | 汇总网址或文件（网页、PDF、图片、音频、YouTube 视频） | Peter Steinberger |
| 7 | **github** | devops | 使用 `gh` CLI 与 GitHub 交互 | Peter Steinberger |
| 8 | **sonoscli** | media | 控制 Sonos 音箱 | Peter Steinberger |
| 9 | **weather** | utils | 获取实时天气与预报（无需 API 密钥） | Peter Steinberger |
| 10 | **proactive-agent** | core | 将 AI 从任务执行者转变为能预见需求的主动伙伴 | halthelobster |
| 11 | **api-gateway** | devops | 通过托管的 OAuth 连接 100+ API | byungkyu |

## 📁 目录结构

```
must-skills/
├── README.md
├── core/                    # 核心评估工具 + 元技能
│   ├── skill-auditor/       # 技能合规性审计
│   ├── skill-evaluator/     # 技能效果评估
│   ├── openclaw-evaluator/  # OpenClaw 系统评估
│   ├── self-improving-agent/# ⭐ 自我改进代理
│   ├── ontology/            # ⭐ 知识图谱
│   ├── find-skills/         # ⭐ 技能发现
│   └── proactive-agent/     # ⭐ 主动式代理
├── feishu/                  # 飞书生态集成
│   ├── doc/                 # 飞书云文档协作
│   ├── drive/               # 飞书云盘文件操作
│   ├── wiki/                # 飞书知识库管理
│   └── perm/                # 飞书权限与安全控制
├── devops/                  # 开发运维
│   ├── github/              # ⭐ GitHub CLI 交互
│   ├── api-gateway/         # ⭐ API 网关
│   ├── github-assistant/    # GitHub 自动化助手
│   ├── git-helper/          # Git 操作辅助
│   ├── code-reviewer/       # 代码审查
│   ├── api-tester/          # API 接口测试
│   ├── log-analyzer/        # 日志分析
│   ├── healthcheck/         # 系统健康检查
│   └── 1password/           # 1Password 凭证管理
├── media/                   # 多媒体处理
│   ├── sonoscli/            # ⭐ Sonos 音箱控制
│   ├── nano-banana-pro/     # AI 图像生成
│   └── video-frames/        # 视频转图片
├── productivity/            # 生产力工具
│   ├── gog/                 # ⭐ Google Workspace CLI
│   ├── tavily-search/       # ⭐ AI 网络搜索
│   ├── summarize/           # ⭐ 内容总结
│   ├── task-planner/        # 任务规划器
│   ├── memory-manager/      # 记忆管理
│   ├── doc-generator/       # 文档生成器
│   ├── file-manager/        # 文件管理
│   └── web-search/          # 网页搜索
└── utils/                   # 基础工具
    ├── skill-creator/       # 技能创建器
    └── weather/             # ⭐ 天气查询
```

## 📊 技能统计

| 分类 | 技能数 | 热门技能 |
|------|--------|---------|
| core | 7 | self-improving-agent, ontology, find-skills, proactive-agent |
| feishu | 4 | doc, drive, wiki, perm |
| devops | 9 | github, api-gateway |
| media | 3 | sonoscli |
| productivity | 8 | gog, tavily-search, summarize |
| utils | 2 | weather |

**总计: 33 个技能**

## 🚀 快速开始

### 安装 Top 10 热门技能

```bash
# 一键安装所有热门技能
for skill in gog self-improving-agent tavily-search ontology find-skills summarize github sonoscli weather proactive-agent api-gateway; do
  openclaw skills install ./must-skills/*/$skill 2>/dev/null || openclaw skills install ./must-skills/*/*/$skill 2>/dev/null
done
```

### 分类批量安装

```bash
# 安装核心工具
for skill in must-skills/core/*/; do
  openclaw skills install "$skill"
done

# 安装生产力工具
for skill in must-skills/productivity/*/; do
  openclaw skills install "$skill"
done
```

### 使用示例

```bash
# Top 1: Google Workspace
gog gmail list --limit 10
gog calendar add "Meeting" --start "14:00"

# Top 3: AI 搜索
tavily-search --query "OpenClaw 最新动态" --depth advanced

# Top 6: 内容总结
summarize --source "https://example.com/article" --length medium

# Top 7: GitHub
github pr list
github issue create --title "Bug" --label bug

# Top 9: 天气
weather --location "北京" --days 3
```

## 🎯 使用场景

### 场景 1: 智能办公自动化

```bash
# 搜索资料 → 总结内容 → 创建文档 → 发送邮件
tavily-search --query "AI 行业趋势 2025" | \
summarize --length long | \
gog docs create --title "AI趋势报告" | \
gog gmail send --to "boss@company.com" --subject "本周报告"
```

### 场景 2: 开发工作流

```bash
# 代码审查 → 创建 PR → 运行测试
code-reviewer --path ./src | \
github pr create --title "Feature: xxx" | \
api-tester --run
```

### 场景 3: 智能家居

```bash
# 天气查询 → 调整音箱 → 发送提醒
weather --location "上海" | \
sonoscli --room "客厅" --action play --playlist "轻音乐"
```

## 🔧 配置指南

### Google Workspace (gog)
```bash
# 需要配置 Google OAuth 凭证
gcloud auth application-default login
```

### Tavily Search
```bash
export TAVILY_API_KEY="your-api-key"
```

### GitHub
```bash
gh auth login
```

### Sonos
```bash
# 自动发现局域网内 Sonos 设备
sonoscli discover
```

## 🤝 贡献

欢迎贡献新的技能！请按功能分类放置在对应目录。

```bash
# 提交新技能
git checkout -b feature/my-skill
git add must-skills/category/my-skill/
git commit -m "feat(category): add my-skill"
git push origin feature/my-skill
```

## 📄 许可证

MIT License

## 🙏 致谢

- [ClawHub](https://clawhub.ai) - 官方技能市场
- [Awesome OpenClaw Skills](https://github.com/VoltAgent/awesome-openclaw-skills) - 社区技能索引
- OpenClaw 创始人 Peter Steinberger 及所有技能作者

---

**维护者**: yanjiayi-bd  
**最后更新**: 2025-01
