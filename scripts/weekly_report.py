#!/usr/bin/env python3
"""
Weekly Report Generator for ClawHub Skills Sync
生成每周学习报告
"""

import json
from datetime import datetime
from pathlib import Path

MUST_SKILLS_DIR = Path("/workspace/projects/must-skills")
TRACK_FILE = MUST_SKILLS_DIR / ".skill-track.json"
REPORT_DIR = MUST_SKILLS_DIR / "reports"


def generate_weekly_report():
    """生成周报告"""
    
    if not TRACK_FILE.exists():
        print("暂无追踪数据")
        return
    
    with open(TRACK_FILE, "r") as f:
        data = json.load(f)
    
    stats = data.get("stats", {})
    history = stats.get("weekly_history", [])
    
    if not history:
        print("暂无历史记录")
        return
    
    # 获取本周数据
    current_week = history[-1]
    
    # 创建报告目录
    REPORT_DIR.mkdir(exist_ok=True)
    
    # 生成报告文件名
    week_str = datetime.now().strftime("%Y-W%W")
    report_file = REPORT_DIR / f"weekly-report-{week_str}.md"
    
    # 生成报告内容
    report = f"""# ClawHub Skills 周学习报告

**报告周期**: {week_str}  
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 本周统计

| 指标 | 数值 |
|------|------|
| 新学习技能 | {current_week.get('new', 0)} |
| 更新技能 | {current_week.get('updated', 0)} |
| 跳过（已最新） | {current_week.get('skipped', 0)} |

## 🎯 处理的技能

{chr(10).join(f"- {s}" for s in current_week.get('skills', []))}

## 📈 累计统计

- **累计学习**: {stats.get('total_learned', 0)} 个技能
- **累计更新**: {stats.get('total_updated', 0)} 次
- **追踪周数**: {len(history)} 周

## 📚 已追踪技能列表

{generate_tracked_skills_table(data.get('tracked_skills', {}))}

## 🔗 相关链接

- [ClawHub 技能市场](https://clawhub.ai/skills?sort=downloads)
- [must-skills GitHub 仓库](https://github.com/yanjiayi-bd/must-skills)
- [完整追踪数据](./../.skill-track.json)

---
*此报告由自动同步系统生成*
"""
    
    with open(report_file, "w") as f:
        f.write(report)
    
    print(f"✓ 周报告已生成: {report_file}")
    print(report)


def generate_tracked_skills_table(tracked_skills: dict) -> str:
    """生成已追踪技能表格"""
    
    if not tracked_skills:
        return "暂无追踪的技能"
    
    table = "| 技能名称 | 版本 | 状态 | 最后检查 |\n"
    table += "|---------|------|------|----------|\n"
    
    for name, info in sorted(tracked_skills.items()):
        version = info.get('version', '-')
        status = info.get('status', '-')
        last_check = info.get('last_check', '-')[:10]  # 只显示日期
        
        status_emoji = {
            "learned": "✅",
            "updated": "🔄",
            "skipped": "⏭️"
        }.get(status, "❓")
        
        table += f"| {name} | {version} | {status_emoji} {status} | {last_check} |\n"
    
    return table


if __name__ == "__main__":
    generate_weekly_report()
