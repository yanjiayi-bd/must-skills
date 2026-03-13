# Auto-Updater

每日自动更新 OpenClaw 及其所有已安装技能，通过定时任务检查、应用更新，并向用户发送变更摘要。

## 功能

### 1. 自动检查更新
- 每日定时检查 OpenClaw 新版本
- 扫描所有已安装技能的更新
- 检测安全补丁和重要修复

### 2. 智能更新策略
- 自动应用补丁更新
- 等待用户确认重大版本更新
- 回滚机制（更新失败时）

### 3. 变更摘要
- 生成更新日志摘要
- 高亮重要变更
- 标记破坏性变更

### 4. 定时任务管理
- 配置检查频率
- 设置更新时段
- 自定义更新规则

## 配置

```json
{
  "autoUpdater": {
    "enabled": true,
    "checkInterval": "daily",
    "checkTime": "02:00",
    "autoApply": {
      "patches": true,
      "minor": false,
      "major": false
    },
    "exclude": ["sensitive-skill"],
    "notifications": {
      "onUpdate": true,
      "onError": true
    }
  }
}
```

## 使用

```bash
# 手动检查更新
auto-updater check

# 立即更新所有
auto-updater update --all

# 查看更新日志
auto-updater changelog

# 配置自动更新
auto-updater config --enable --time "03:00"

# 暂停自动更新
auto-updater pause

# 恢复自动更新
auto-updater resume
```

## 输出示例

```
[Auto-Updater] 2026-03-13 02:00:01
检查更新...

发现更新:
✓ OpenClaw: 2026.3.8 → 2026.3.11
✓ tavily-search: 1.0.0 → 1.0.2
✓ github: 1.0.0 → 1.1.0

已自动更新:
✓ tavily-search (patch)

等待确认:
⚠ OpenClaw (minor) - 包含 breaking changes

更新完成!
```

## 最佳实践

- 在低峰时段运行更新
- 更新前自动备份配置
- 生产环境谨慎开启 autoApply
- 定期检查更新日志
