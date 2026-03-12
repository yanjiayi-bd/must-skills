# Must Skills - OpenClaw 技能集合

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> 一套精选的 OpenClaw Agent 技能工具，用于审计、评估和管理其他技能。

## 📁 项目结构

```
must-skills/
├── README.md                   # 项目说明
├── skill-auditor/              # Skill 安全审计工具
│   ├── skill.json              # 技能配置
│   └── prompt.md               # 提示词定义
├── skill-evaluator/            # Skill 价值评估工具
│   ├── skill.json              # 技能配置
│   └── prompt.md               # 提示词定义
└── openclaw-evaluator/         # OpenClaw 能力等级鉴定工具
    ├── skill.json              # 技能配置
    └── prompt.md               # 提示词定义
```

## 🛠️ 技能列表

### 1. Skill Auditor - 技能安全审计工具

**功能特性：**
- 四级风险定义 (P0-P3)
- 三大审计模块 (意图识别/工具权限/输出清洗)
- 安全扫描和代码审查
- 修复优先级建议

### 2. Skill Evaluator - 技能价值评估工具

**功能特性：**
- VQI 价值评估模型
- 四大维度评分 (TSR/AL/ROI/SR)
- 业务模块分类
- 安装优先级建议

### 3. OpenClaw Evaluator - 能力等级鉴定工具

**功能特性：**
- 八级学术等级评定 (幼儿园→博士后)
- 四大考核维度 (D1-D4)
- 认知深度与工程稳定性评估
- 进化路线图生成

## 🚀 快速开始

### 安装单个技能

```bash
# 安装 skill-auditor
cd skill-auditor
openclaw skills install .

# 安装 skill-evaluator  
cd skill-evaluator
openclaw skills install .

# 安装 openclaw-evaluator
cd openclaw-evaluator
openclaw skills install .
```

### 使用技能

```bash
# 审计技能安全性
openclaw skills audit <skill-name>

# 评估技能价值
openclaw skills evaluate <skill-name>

# 鉴定 OpenClaw 能力等级
openclaw skills assess --config openclaw.json --logs execution.log
```

## 📖 文档

| 技能 | 文档 |
|------|------|
| Skill Auditor | [skill-auditor/prompt.md](./skill-auditor/prompt.md) |
| Skill Evaluator | [skill-evaluator/prompt.md](./skill-evaluator/prompt.md) |
| OpenClaw Evaluator | [openclaw-evaluator/prompt.md](./openclaw-evaluator/prompt.md) |

## 🤝 贡献

欢迎提交 Issue 和 PR！

## 📄 许可证

MIT License
