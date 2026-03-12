# Must Skills - OpenClaw 技能集合

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-13-orange)](./)

> 一套精选的 OpenClaw Agent 技能工具，精选自 ClawHub Top 10 热门技能。

## 📁 项目结构

```
must-skills/
├── README.md                   # 项目说明
├── skill-auditor/              # Skill 安全审计工具
├── skill-evaluator/            # Skill 价值评估工具
├── openclaw-evaluator/         # OpenClaw 能力等级鉴定工具
├── web-search/                 # 网络搜索 (Top 1 ⭐)
├── github-assistant/           # GitHub 助手 (Top 2 ⭐)
├── file-manager/               # 文件管理器 (Top 3 ⭐)
├── code-reviewer/              # 代码审查 (Top 4 ⭐)
├── task-planner/               # 任务规划师 (Top 5 ⭐)
├── memory-manager/             # 记忆管理器 (Top 6 ⭐)
├── api-tester/                 # API 测试工具 (Top 7 ⭐)
├── doc-generator/              # 文档生成器 (Top 8 ⭐)
├── git-helper/                 # Git 助手 (Top 9 ⭐)
└── log-analyzer/               # 日志分析器 (Top 10 ⭐)
```

## 🛠️ 技能列表

### 核心评估工具 (3个)

| 技能 | 功能 | 用途 |
|------|------|------|
| **skill-auditor** | 四级风险安全审计 | 审计 Skill 安全性 |
| **skill-evaluator** | VQI 价值评估模型 | 评估 Skill 价值 |
| **openclaw-evaluator** | 八级能力等级鉴定 | 评估 Agent 能力 |

### ClawHub Top 10 复刻 (10个)

| 排名 | 技能 | 功能描述 | 标签 |
|-----|------|---------|------|
| ⭐ 1 | **web-search** | 多引擎网络搜索和信息整合 | search, web, research |
| ⭐ 2 | **github-assistant** | 仓库管理、Issue/PR 处理、代码审查 | github, devops, code |
| ⭐ 3 | **file-manager** | 智能文件管理、批量处理、目录分析 | file, filesystem, batch |
| ⭐ 4 | **code-reviewer** | 自动化代码检查、质量评估、改进建议 | code, review, quality |
| ⭐ 5 | **task-planner** | 智能任务分解、执行计划、进度跟踪 | task, planning, productivity |
| ⭐ 6 | **memory-manager** | 智能记忆存储、检索、关联和压缩 | memory, storage, context |
| ⭐ 7 | **api-tester** | 接口测试、性能测试、文档生成 | api, test, http |
| ⭐ 8 | **doc-generator** | 自动生成代码文档、API 文档 | doc, documentation, markdown |
| ⭐ 9 | **git-helper** | 版本控制、分支管理、冲突解决 | git, version-control |
| ⭐ 10 | **log-analyzer** | 日志解析、错误检测、趋势分析 | log, analysis, monitoring |

## 🚀 快速开始

### 安装单个技能

```bash
# 安装网络搜索技能
cd web-search
openclaw skills install .

# 安装 GitHub 助手
cd github-assistant
openclaw skills install .

# 安装代码审查工具
cd code-reviewer
openclaw skills install .
```

### 使用技能

```bash
# 执行网络搜索
openclaw skills run web-search --query "OpenClaw 最新版本"

# 审查代码
openclaw skills run code-reviewer --code "./src" --language "typescript"

# 生成文档
openclaw skills run doc-generator --source "./src" --type "api"
```

## 📊 技能对比

### 开发工具类
| 技能 | 主要功能 | 适用场景 |
|------|---------|---------|
| code-reviewer | 代码质量检查 | 代码提交前审查 |
| github-assistant | GitHub 操作 | 开源项目管理 |
| git-helper | Git 操作 | 版本控制 |
| doc-generator | 文档生成 | 项目文档维护 |
| api-tester | 接口测试 | API 开发测试 |

### 效率工具类
| 技能 | 主要功能 | 适用场景 |
|------|---------|---------|
| web-search | 信息检索 | 调研、学习 |
| file-manager | 文件管理 | 批量处理文件 |
| task-planner | 任务规划 | 项目管理 |
| memory-manager | 记忆管理 | 长期对话保持 |
| log-analyzer | 日志分析 | 系统监控 |

## 📖 文档

| 类别 | 技能 | 文档 |
|------|------|------|
| 评估 | skill-auditor | [skill-auditor/prompt.md](./skill-auditor/prompt.md) |
| 评估 | skill-evaluator | [skill-evaluator/prompt.md](./skill-evaluator/prompt.md) |
| 评估 | openclaw-evaluator | [openclaw-evaluator/prompt.md](./openclaw-evaluator/prompt.md) |
| 搜索 | web-search | [web-search/prompt.md](./web-search/prompt.md) |
| 开发 | github-assistant | [github-assistant/prompt.md](./github-assistant/prompt.md) |
| 开发 | code-reviewer | [code-reviewer/prompt.md](./code-reviewer/prompt.md) |
| 开发 | api-tester | [api-tester/prompt.md](./api-tester/prompt.md) |
| 开发 | doc-generator | [doc-generator/prompt.md](./doc-generator/prompt.md) |
| 开发 | git-helper | [git-helper/prompt.md](./git-helper/prompt.md) |
| 效率 | file-manager | [file-manager/prompt.md](./file-manager/prompt.md) |
| 效率 | task-planner | [task-planner/prompt.md](./task-planner/prompt.md) |
| 效率 | memory-manager | [memory-manager/prompt.md](./memory-manager/prompt.md) |
| 效率 | log-analyzer | [log-analyzer/prompt.md](./log-analyzer/prompt.md) |

## 🎯 使用场景

### 场景 1: 新项目启动
```bash
# 1. 规划任务
openclaw skills run task-planner --goal "启动新项目"

# 2. 生成项目文档
openclaw skills run doc-generator --source "./" --type "readme"

# 3. 初始化 Git
openclaw skills run git-helper --command "init"
```

### 场景 2: 代码审查流程
```bash
# 1. 审查代码
openclaw skills run code-reviewer --code "./src" --language "python"

# 2. 运行测试
openclaw skills run api-tester --url "http://localhost:8080"

# 3. 提交到 GitHub
openclaw skills run github-assistant --action "pr" --repo "owner/repo"
```

### 场景 3: 系统监控
```bash
# 1. 分析日志
openclaw skills run log-analyzer --log_source "/var/log/app.log"

# 2. 搜索解决方案
openclaw skills run web-search --query "如何解决 {error}"

# 3. 生成报告
openclaw skills run doc-generator --type "wiki"
```

## 🤝 贡献

欢迎提交 Issue 和 PR！

### 添加新技能
1. 创建 `{skill-name}/skill.json`
2. 创建 `{skill-name}/prompt.md`
3. 更新 README.md
4. 提交 PR

## 📄 许可证

MIT License

## 🙏 致谢

技能设计参考自 [ClawHub](https://clawhub.ai) 热门技能排行榜
