# 🔄 ClawHub Top 10 自动同步系统

每周自动学习、安装、复刻 ClawHub 热门技能的完整自动化方案。

## 📋 系统概述

这个系统自动完成以下任务：

1. **每周获取** ClawHub Top 10 热门技能
2. **自动学习** 新技能并安装到 OpenClaw
3. **版本检查** 已学习技能的更新
4. **自动复刻** 到 must-skills GitHub 仓库
5. **完整性检查** 验证技能文件完整性
6. **生成报告** 每周学习进度报告

## 🏗️ 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│                    Auto Sync System                          │
├─────────────────────────────────────────────────────────────┤
│  Cron (每周一 2:00 AM)                                       │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐   │
│  │  clawhub_sync │───▶│ SkillTracker │───▶│   GitHub     │   │
│  │    .py       │    │  (版本追踪)   │    │   Push       │   │
│  └──────────────┘    └──────────────┘    └──────────────┘   │
│         │                    │                              │
│         ▼                    ▼                              │
│  ┌──────────────┐    ┌──────────────┐                       │
│  │  OpenClaw    │    │ .skill-track │                       │
│  │   Install    │    │   .json      │                       │
│  └──────────────┘    └──────────────┘                       │
│         │                                                   │
│         ▼                                                   │
│  ┌──────────────┐                                           │
│  │ INTEGRITY_   │                                           │
│  │ REPORT.md    │                                           │
│  └──────────────┘                                           │
└─────────────────────────────────────────────────────────────┘
```

## 📁 文件说明

| 文件 | 说明 |
|------|------|
| `scripts/clawhub_sync.py` | 主同步脚本（Python） |
| `scripts/clawhub-sync.sh` | 备用同步脚本（Bash） |
| `scripts/weekly_report.py` | 周报生成器 |
| `scripts/setup.sh` | 系统安装脚本 |
| `scripts/crontab.txt` | 定时任务配置 |
| `.skill-track.json` | 技能版本追踪数据库 |
| `INTEGRITY_REPORT.md` | 完整性检查报告 |

## ✅ 完整性检查规则

每次同步运行时，系统会自动检查所有技能的完整性：

### 检查项

| 规则 | 说明 | 优先级 |
|------|------|--------|
| **metadata.emoji** | skill.json 必须包含 `metadata.clawdbot.emoji` | 🔴 必须 |
| **原始作者标注** | 复刻技能必须保留原始作者信息 | 🔴 必须 |
| **inputs/outputs** | Top 10 技能应有完整的输入输出定义 | 🟡 建议 |
| **prompt.md 详细度** | prompt.md 应包含使用示例和输出格式 | 🟡 建议 |

### 检查示例

```bash
$ python3 scripts/clawhub_sync.py
[ integrity check ] 运行技能完整性检查...
✓ 技能 gog 完整
✓ 技能 self-improving-agent 完整
⚠ 技能 find-skills 不完整:
  - 缺少 metadata.clawdbot.emoji
  - prompt.md 内容过于简单 (120 字符)
✓ 技能 summarize 完整
...
完整性检查完成: 30/33 技能完整
```

### 完整性报告

自动生成 `INTEGRITY_REPORT.md`：

```markdown
# Skill 完整性检查报告

## 统计
- 总技能数: 33
- 完整技能: 30
- 不完整技能: 3
- 完整率: 90.9%

## 需要完善的技能

### find-skills (core/find-skills)
- [ ] 缺少 metadata.clawdbot.emoji
- [ ] prompt.md 内容过于简单 (120 字符)

### weather (utils/weather)
- [ ] 缺少完整的 inputs 定义

## 检查规则
1. skill.json 必须包含 `metadata.clawdbot.emoji`
2. 复刻技能必须明确标注原始作者
3. Top 10 技能应有完整的 inputs/outputs 定义
4. prompt.md 应包含详细的使用说明和示例
```

## 🚀 快速开始

### 1. 安装系统

```bash
cd /workspace/projects/must-skills
./scripts/setup.sh
```

### 2. 手动运行同步

```bash
# 立即执行一次同步
python3 scripts/clawhub_sync.py
```

### 3. 生成周报告

```bash
python3 scripts/weekly_report.py
```

## ⏰ 定时任务配置

系统默认配置：

```cron
# 每周一凌晨 2:00 自动同步
0 2 * * 1 python3 scripts/clawhub_sync.py

# 每周日上午 10:00 生成周报
0 10 * * 0 python3 scripts/weekly_report.py
```

### 自定义定时

```bash
# 编辑定时任务
crontab -e

# 查看当前定时任务
crontab -l
```

## 📊 技能追踪系统

### 追踪文件结构

`.skill-track.json`:

```json
{
  "last_sync": "2026-03-12T19:22:45",
  "tracked_skills": {
    "gog": {
      "version": "1.0.0",
      "status": "learned",
      "last_check": "2026-03-12T19:22:45"
    }
  },
  "stats": {
    "total_learned": 10,
    "total_updated": 0,
    "weekly_history": [...]
  }
}
```

### 状态说明

| 状态 | 含义 |
|------|------|
| `learned` | 新学习并安装 |
| `updated` | 版本更新 |
| `skipped` | 已是最新，跳过 |

## 🔧 工作流程

### 每周同步流程

1. **获取榜单** → 从 ClawHub 获取 Top 10 技能
2. **检查版本** → 对比已追踪技能的版本
3. **处理新技能** → 创建文件 → 安装 → 激活
4. **处理更新** → 更新版本 → 重新安装
5. **跳过最新** → 版本相同则跳过
6. **GitHub 同步** → 提交并推送变更
7. **记录统计** → 更新追踪文件

### 首次运行示例

```
[1/10] 检查技能: gog (v1.0.0)
  → 新技能，开始学习和安装
  ✓ 技能文件已创建
  ✓ 已安装到 ~/.openclaw/skills/gog
  ✓ 已激活并准备好使用

[2/10] 检查技能: self-improving-agent (v1.0.0)
  → 新技能，开始学习和安装
  ...

同步完成!
  本次新学习: 10
  本次更新: 0
  本次跳过: 0
  累计学习: 10
```

### 后续运行示例

```
[1/10] 检查技能: gog (v1.1.0)
  → 发现新版本 (1.0.0 → 1.1.0)，开始更新
  ✓ 版本已更新
  ✓ 已重新安装

[2/10] 检查技能: self-improving-agent (v1.0.0)
  → 已是最新版本，跳过

同步完成!
  本次新学习: 0
  本次更新: 1
  本次跳过: 9
```

## 📈 周报内容

每周自动生成报告：`reports/weekly-report-YYYY-WWW.md`

包含：
- 本周统计（新学习/更新/跳过）
- 处理的技能列表
- 累计统计
- 已追踪技能完整表格

## 🛠️ 高级配置

### 修改技能分类

编辑 `clawhub_sync.py` 中的分类映射：

```python
CATEGORY_MAP = {
    "gog": "productivity",
    "github": "devops",
    "sonoscli": "media",
    # ...
}
```

### 添加自定义技能源

可以扩展 `fetch_clawhub_top10()` 方法支持多个数据源：

```python
def fetch_clawhub_top10(self) -> List[Dict]:
    # 1. 从 ClawHub 获取
    # 2. 从 GitHub API 获取
    # 3. 从本地缓存获取
    pass
```

### 集成 Webhook 通知

在同步完成后添加通知：

```python
def send_notification(self, stats):
    # 发送到 Slack/钉钉/邮件
    pass
```

## 🔍 故障排查

### 查看日志

```bash
# 同步日志
tail -f /tmp/clawhub-sync.log

# Cron 日志
tail -f /tmp/clawhub-cron.log
```

### 手动重置追踪

```bash
# 重置特定技能
jq 'del(.tracked_skills["skill-name"])' .skill-track.json > tmp.json && mv tmp.json .skill-track.json

# 完全重置（谨慎使用）
echo '{"last_sync": "", "tracked_skills": {}, "stats": {"total_learned": 0, "total_updated": 0, "weekly_history": []}}' > .skill-track.json
```

### 强制重新安装

```bash
# 删除已安装的技能
rm -rf ~/.openclaw/skills/skill-name

# 删除追踪记录
# 然后重新运行同步
```

## 📝 更新计划

### 短期优化
- [ ] 添加 Slack/钉钉通知
- [ ] 支持技能评分和反馈
- [ ] 自动截图技能使用示例

### 长期规划
- [ ] Web UI 管理界面
- [ ] 技能使用数据分析
- [ ] 智能推荐相关技能

## 🤝 贡献

欢迎改进自动同步系统！可以提交：
- 新的数据源适配器
- 更好的错误处理
- 更多的通知渠道
- 性能优化

## 📄 许可证

MIT License
