#!/bin/bash
# Setup script for ClawHub Auto Sync System

set -e

echo "🦞 ClawHub Auto Sync System Setup"
echo "=================================="
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi
echo "✓ Python3 已安装"

# 检查 pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 未安装"
    exit 1
fi
echo "✓ pip3 已安装"

# 安装依赖
echo ""
echo "📦 安装依赖..."
pip3 install -q pathlib 2>/dev/null || true
echo "✓ 依赖安装完成"

# 创建必要目录
echo ""
echo "📁 创建目录结构..."
mkdir -p /workspace/projects/must-skills/{scripts,reports}
mkdir -p ~/.openclaw/skills
echo "✓ 目录创建完成"

# 设置脚本权限
echo ""
echo "🔧 设置脚本权限..."
chmod +x /workspace/projects/must-skills/scripts/*.py
chmod +x /workspace/projects/must-skills/scripts/*.sh
echo "✓ 权限设置完成"

# 初始化追踪文件
echo ""
echo "📝 初始化追踪文件..."
if [[ ! -f /workspace/projects/must-skills/.skill-track.json ]]; then
    cat > /workspace/projects/must-skills/.skill-track.json << 'EOF'
{
  "last_sync": "",
  "tracked_skills": {},
  "stats": {
    "total_learned": 0,
    "total_updated": 0,
    "weekly_history": []
  }
}
EOF
    echo "✓ 追踪文件已创建"
else
    echo "✓ 追踪文件已存在"
fi

# 安装 cron 任务
echo ""
echo "⏰ 安装定时任务..."
if command -v crontab &> /dev/null; then
    # 备份现有 crontab
    crontab -l > /tmp/crontab.backup 2>/dev/null || true
    
    # 安装新 crontab
    crontab /workspace/projects/must-skills/scripts/crontab.txt
    echo "✓ 定时任务已安装"
    echo ""
    echo "📋 当前定时任务:"
    crontab -l | grep -v "^#" | grep -v "^$" || echo "  (无)"
else
    echo "⚠️  crontab 命令不可用，请手动安装定时任务:"
    echo "   cat scripts/crontab.txt | crontab -"
fi

echo ""
echo "=================================="
echo "✅ 设置完成!"
echo ""
echo "使用方法:"
echo "  1. 手动运行同步: python3 scripts/clawhub_sync.py"
echo "  2. 生成周报告:   python3 scripts/weekly_report.py"
echo "  3. 查看日志:     tail -f /tmp/clawhub-sync.log"
echo ""
echo "自动同步计划:"
echo "  - 每周一凌晨 2:00 自动同步 ClawHub Top 10"
echo "  - 每周日上午 10:00 生成周报"
echo ""
echo "现在可以运行测试: python3 scripts/clawhub_sync.py"
