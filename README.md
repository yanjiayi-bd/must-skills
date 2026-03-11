# Must Skills - OpenClaw 技能集合

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> 一套精选的 OpenClaw Agent 技能工具，用于审计、评估和管理其他技能。

## 📁 项目结构

```
must-skills/
├── README.md                   # 项目说明
├── skill-auditor/              # Skill 审计工具
│   ├── skill.json              # 技能配置
│   └── prompt.md               # 提示词定义
└── skill-evaluator/            # Skill 价值评估工具
    ├── skill.json              # 技能配置
    └── prompt.md               # 提示词定义
```

## 🛠️ 技能列表

### 1. Skill Auditor - 技能审计工具

安全扫描和审查 Skill 代码，检测潜在风险。

**功能特性：**
- 代码安全扫描
- 依赖漏洞检测
- 权限审计
- 风险评估报告

### 2. Skill Evaluator - 技能价值评估工具

评估 Skill 的价值和使用建议。

**功能特性：**
- 功能价值分析
- 使用场景匹配
- 效率提升评估
- 安装优先级建议

## 🚀 快速开始

### 安装单个技能

```bash
# 安装 skill-auditor
cd skill-auditor
openclaw skills install .

# 安装 skill-evaluator  
cd skill-evaluator
openclaw skills install .
```

### 使用技能

```bash
# 审计技能
openclaw skills audit <skill-name>

# 评估技能价值
openclaw skills evaluate <skill-name>
```

## 📖 文档

- [Skill Auditor 文档](./skill-auditor/README.md)
- [Skill Evaluator 文档](./skill-evaluator/README.md)

## 🤝 贡献

欢迎提交 Issue 和 PR！

## 📄 许可证

MIT License
