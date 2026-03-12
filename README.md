# Must-Skills for OpenClaw

精选 OpenClaw 高价值技能集合，按功能分类组织，便于查找和使用。

## 📁 目录结构

```
must-skills/
├── README.md
├── core/                    # 核心评估工具
│   ├── skill-auditor/       # 技能合规性审计
│   ├── skill-evaluator/     # 技能效果评估
│   └── openclaw-evaluator/  # OpenClaw 系统评估
├── feishu/                  # 飞书生态集成
│   ├── doc/                 # 飞书云文档协作
│   ├── drive/               # 飞书云盘文件操作
│   ├── wiki/                # 飞书知识库管理
│   └── perm/                # 飞书权限与安全控制
├── devops/                  # 开发运维
│   ├── github-assistant/    # GitHub 自动化助手
│   ├── git-helper/          # Git 操作辅助
│   ├── code-reviewer/       # 代码审查
│   ├── api-tester/          # API 接口测试
│   ├── log-analyzer/        # 日志分析
│   ├── healthcheck/         # 系统健康检查
│   └── 1password/           # 1Password 凭证管理
├── media/                   # 多媒体处理
│   ├── nano-banana-pro/     # Gemini 图像生成
│   └── video-frames/        # FFmpeg 视频转图片
├── productivity/            # 生产力工具
│   ├── task-planner/        # 任务规划器
│   ├── memory-manager/      # 记忆管理
│   ├── doc-generator/       # 文档生成器
│   ├── file-manager/        # 文件管理
│   └── web-search/          # 网页搜索
└── utils/                   # 基础工具
    ├── skill-creator/       # 技能创建器
    └── weather/             # 天气查询
```

## 📊 技能矩阵

### Core - 核心评估

| 技能 | 描述 | 用途 |
|------|------|------|
| `skill-auditor` | 技能合规性审计 | 检查技能是否符合规范 |
| `skill-evaluator` | 技能效果评估 | 评估技能执行质量 |
| `openclaw-evaluator` | OpenClaw 系统评估 | 系统级性能评估 |

### Feishu - 飞书生态

| 技能 | 描述 | 用途 |
|------|------|------|
| `doc` | 飞书云文档协作 | 文档创建、编辑、协作 |
| `drive` | 飞书云盘文件操作 | 文件上传、下载、管理 |
| `wiki` | 飞书知识库管理 | 知识库浏览、搜索、编辑 |
| `perm` | 飞书权限管理 | 权限配置、安全审计 |

### DevOps - 开发运维

| 技能 | 描述 | 用途 |
|------|------|------|
| `github-assistant` | GitHub 自动化 | PR、Issue、Actions 管理 |
| `git-helper` | Git 操作辅助 | 分支、提交、合并辅助 |
| `code-reviewer` | 代码审查 | 自动化代码检查 |
| `api-tester` | API 接口测试 | 接口测试与文档生成 |
| `log-analyzer` | 日志分析 | 日志解析与问题定位 |
| `healthcheck` | 系统健康检查 | 服务状态监控 |
| `1password` | 1Password 集成 | 凭证管理与安全访问 |

### Media - 多媒体

| 技能 | 描述 | 用途 |
|------|------|------|
| `nano-banana-pro` | AI 图像生成 | Gemini 文生图 |
| `video-frames` | 视频处理 | 视频转图片序列 |

### Productivity - 生产力

| 技能 | 描述 | 用途 |
|------|------|------|
| `task-planner` | 任务规划 | 智能任务分解与排期 |
| `memory-manager` | 记忆管理 | 对话记忆持久化 |
| `doc-generator` | 文档生成 | 自动化文档创建 |
| `file-manager` | 文件管理 | 文件操作与组织 |
| `web-search` | 网页搜索 | 实时信息检索 |

### Utils - 基础工具

| 技能 | 描述 | 用途 |
|------|------|------|
| `skill-creator` | 技能创建器 | 快速创建新技能 |
| `weather` | 天气查询 | 实时天气与预报 |

## 🚀 快速开始

### 安装单个分类的所有技能

```bash
# 安装所有飞书技能
for skill in must-skills/feishu/*/; do
  openclaw skills install "$skill"
done

# 安装所有 DevOps 技能
for skill in must-skills/devops/*/; do
  openclaw skills install "$skill"
done
```

### 安装单个技能

```bash
openclaw skills install ./must-skills/utils/weather
openclaw skills install ./must-skills/feishu/doc
openclaw skills install ./must-skills/devops/healthcheck
```

### 使用技能

```bash
# 查看已安装技能
openclaw skills list

# 运行技能
openclaw skills run weather --input location="北京"
openclaw skills run feishu/doc --input action="list"
openclaw skills run devops/healthcheck --input target="all"
```

## 🎯 使用场景

### 场景 1：飞书办公自动化

```bash
# 批量导出部门文档
openclaw skills run feishu/doc --input action="export" --input folder="项目文档"

# 设置团队权限
openclaw skills run feishu/perm --input action="grant" --input user="team@company.com"

# 搜索知识库
openclaw skills run feishu/wiki --input action="search" --input query="API 规范"
```

### 场景 2：DevOps 日常运维

```bash
# 系统健康检查
openclaw skills run devops/healthcheck --input target="all" --input notify=true

# 获取生产环境凭证
openclaw skills run devops/1password --input action="get" --input item="prod-db"

# 分析应用日志
openclaw skills run devops/log-analyzer --input file="/var/log/app.log"

# 代码审查
openclaw skills run devops/code-reviewer --input path="./src"
```

### 场景 3：内容创作

```bash
# 生成配图
openclaw skills run media/nano-banana-pro --input prompt="科技感办公场景"

# 提取视频封面
openclaw skills run media/video-frames --input video="demo.mp4" --input frame="00:00:05"

# 搜索素材
openclaw skills run productivity/web-search --input query="2024 设计趋势"
```

### 场景 4：项目管理

```bash
# 创建任务计划
openclaw skills run productivity/task-planner --input goal="上线新功能"

# 生成项目文档
openclaw skills run productivity/doc-generator --input type="api"

# 管理项目文件
openclaw skills run productivity/file-manager --input action="organize"
```

## 🔧 配置指南

### Feishu 集成

在 `openclaw.json` 中配置：

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

```bash
# 安装 1Password CLI
brew install 1password-cli

# 登录
op account add --address my.1password.com --email user@example.com
```

### Gemini API

```bash
export GEMINI_API_KEY="your-api-key"
```

## 🤝 贡献指南

欢迎提交新的技能！请按以下步骤：

1. **选择分类**：根据功能选择合适的分类目录
2. **创建技能**：每个技能一个独立子目录
3. **必需文件**：
   - `skill.json` - 技能配置
   - `prompt.md` - 提示词定义
4. **可选文件**：
   - `README.md` - 详细说明
   - `examples/` - 使用示例

```bash
# 示例：提交新的 DevOps 技能
git checkout -b feature/new-devops-skill
mkdir -p must-skills/devops/my-skill
cp skill.json prompt.md must-skills/devops/my-skill/
git add must-skills/devops/my-skill/
git commit -m "feat(devops): add my-skill for ..."
git push origin feature/new-devops-skill
```

## 📄 许可证

MIT License - 详见 [LICENSE](../LICENSE)

---

**维护者**: yanjiayi-bd  
**最后更新**: 2025-01
