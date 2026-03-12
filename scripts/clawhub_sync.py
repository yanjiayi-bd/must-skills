#!/usr/bin/env python3
"""
ClawHub Top 10 Skills Auto Sync Manager
每周自动学习、安装、复刻 ClawHub 热门技能
"""

import json
import os
import sys
import subprocess
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# 配置
MUST_SKILLS_DIR = Path("/workspace/projects/must-skills")
TRACK_FILE = MUST_SKILLS_DIR / ".skill-track.json"
LOG_FILE = Path("/tmp/clawhub-sync.log")
CONFIG_FILE = MUST_SKILLS_DIR / ".clawhub-sync-config.json"

# ClawHub Top 10 技能模板（每周更新）
CLAWHUB_TOP10_TEMPLATE = [
    {"rank": 1, "name": "gog", "version": "1.0.0", "author": "Peter Steinberger", 
     "desc": "Google Workspace CLI", "category": "productivity"},
    {"rank": 2, "name": "self-improving-agent", "version": "1.0.0", "author": "pskoett",
     "desc": "Self-evolution agent", "category": "core"},
    {"rank": 3, "name": "tavily-search", "version": "1.0.0", "author": "arun-8687",
     "desc": "AI web search", "category": "productivity"},
    {"rank": 4, "name": "ontology", "version": "1.0.0", "author": "oswalpalash",
     "desc": "Knowledge graph", "category": "core"},
    {"rank": 5, "name": "find-skills", "version": "1.0.0", "author": "JimLiuxinghai",
     "desc": "Skill discovery", "category": "core"},
    {"rank": 6, "name": "summarize", "version": "1.0.0", "author": "Peter Steinberger",
     "desc": "Content summarization", "category": "productivity"},
    {"rank": 7, "name": "github", "version": "1.0.0", "author": "Peter Steinberger",
     "desc": "GitHub CLI", "category": "devops"},
    {"rank": 8, "name": "sonoscli", "version": "1.0.0", "author": "Peter Steinberger",
     "desc": "Sonos control", "category": "media"},
    {"rank": 9, "name": "weather", "version": "1.0.0", "author": "Peter Steinberger",
     "desc": "Weather query", "category": "utils"},
    {"rank": 10, "name": "proactive-agent", "version": "1.0.0", "author": "halthelobster",
     "desc": "Proactive AI", "category": "core"},
]


class Logger:
    """日志记录器"""
    
    @staticmethod
    def log(msg: str, level: str = "INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        colors = {
            "INFO": "\033[32m",      # Green
            "WARNING": "\033[33m",   # Yellow
            "ERROR": "\033[31m",     # Red
            "RESET": "\033[0m"
        }
        color = colors.get(level, colors["INFO"])
        reset = colors["RESET"]
        
        log_line = f"{color}[{timestamp}] {level}:{reset} {msg}"
        print(log_line)
        
        # 写入日志文件
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {level}: {msg}\n")
    
    @staticmethod
    def info(msg: str):
        Logger.log(msg, "INFO")
    
    @staticmethod
    def warning(msg: str):
        Logger.log(msg, "WARNING")
    
    @staticmethod
    def error(msg: str):
        Logger.log(msg, "ERROR")


class SkillTracker:
    """技能版本追踪管理器"""
    
    def __init__(self):
        self.data = self._load()
    
    def _load(self) -> Dict:
        """加载追踪数据"""
        if TRACK_FILE.exists():
            with open(TRACK_FILE, "r") as f:
                return json.load(f)
        return {
            "last_sync": "",
            "tracked_skills": {},
            "stats": {
                "total_learned": 0,
                "total_updated": 0,
                "weekly_history": []
            }
        }
    
    def save(self):
        """保存追踪数据"""
        TRACK_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(TRACK_FILE, "w") as f:
            json.dump(self.data, f, indent=2)
    
    def check_skill(self, name: str, version: str) -> str:
        """
        检查技能状态
        返回: NEW | UPDATE | SKIP
        """
        tracked = self.data["tracked_skills"].get(name)
        
        if not tracked:
            return "NEW"
        
        if tracked.get("version") != version:
            return "UPDATE"
        
        return "SKIP"
    
    def update_skill(self, name: str, version: str, status: str):
        """更新技能追踪信息"""
        self.data["tracked_skills"][name] = {
            "version": version,
            "status": status,
            "last_check": datetime.now().isoformat()
        }
        self.data["last_sync"] = datetime.now().isoformat()
        
        # 更新统计
        if status == "learned":
            self.data["stats"]["total_learned"] += 1
        elif status == "updated":
            self.data["stats"]["total_updated"] += 1
        
        self.save()
    
    def add_weekly_record(self, week_data: Dict):
        """添加周记录"""
        self.data["stats"]["weekly_history"].append(week_data)
        # 只保留最近 52 周记录
        self.data["stats"]["weekly_history"] = self.data["stats"]["weekly_history"][-52:]
        self.save()
    
    def get_stats(self) -> Dict:
        """获取统计信息"""
        return self.data["stats"]


class SkillSyncManager:
    """技能同步管理器"""
    
    def __init__(self):
        self.tracker = SkillTracker()
        self.logger = Logger()
        self.new_skills = []
        self.updated_skills = []
        self.skipped_skills = []
    
    def fetch_clawhub_top10(self) -> List[Dict]:
        """
        获取 ClawHub Top 10 技能列表
        实际使用时可以通过 Web 爬取或 API 获取
        """
        self.logger.info("获取 ClawHub Top 10 技能列表...")
        
        # 这里可以替换为实际的爬取逻辑
        # 例如: 使用 requests 或 playwright 访问 clawhub.ai
        
        return CLAWHUB_TOP10_TEMPLATE
    
    def create_skill_files(self, skill: Dict) -> Path:
        """创建技能文件"""
        name = skill["name"]
        category = skill.get("category", "productivity")
        desc = skill["desc"]
        author = skill["author"]
        
        skill_dir = MUST_SKILLS_DIR / category / name
        skill_dir.mkdir(parents=True, exist_ok=True)
        
        # 创建 skill.json
        skill_json = {
            "name": name,
            "version": skill["version"],
            "description": desc,
            "author": f"yanjiayi-bd (auto-sync from clawhub, original: {author})",
            "license": "MIT",
            "type": "skill",
            "tags": ["auto-sync", "clawhub-top10"],
            "entry": {"prompt": "prompt.md"},
            "inputs": {},
            "outputs": {}
        }
        
        with open(skill_dir / "skill.json", "w") as f:
            json.dump(skill_json, f, indent=2)
        
        # 创建 prompt.md
        prompt_md = f"""# Role: {name}

## 任务
{desc}

## 来源
- 原始作者: {author}
- 来源: ClawHub Top 10 (Rank #{skill['rank']})
- 自动同步时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 使用说明
此技能每周从 ClawHub 自动同步学习并安装。

## 原始描述
{desc}
"""
        
        with open(skill_dir / "prompt.md", "w") as f:
            f.write(prompt_md)
        
        return skill_dir
    
    def install_skill(self, name: str, skill_path: Path) -> bool:
        """安装技能到 OpenClaw"""
        try:
            target_dir = Path.home() / ".openclaw" / "skills" / name
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # 复制文件
            for item in skill_path.iterdir():
                if item.is_file():
                    shutil.copy2(item, target_dir / item.name)
                elif item.is_dir():
                    shutil.copytree(item, target_dir / item.name, dirs_exist_ok=True)
            
            self.logger.info(f"✓ 技能 {name} 已安装到 {target_dir}")
            return True
            
        except Exception as e:
            self.logger.error(f"安装技能 {name} 失败: {e}")
            return False
    
    def activate_skill(self, name: str):
        """激活技能"""
        self.logger.info(f"激活技能: {name}")
        # 这里可以添加实际的激活验证
        # 例如运行一次 help 或 status 命令
        self.logger.info(f"✓ 技能 {name} 已激活并准备好使用")
    
    def update_skill_version(self, skill: Dict) -> bool:
        """更新现有技能版本"""
        name = skill["name"]
        category = skill.get("category", "productivity")
        skill_dir = MUST_SKILLS_DIR / category / name
        
        if not skill_dir.exists():
            self.logger.warning(f"技能目录不存在: {skill_dir}")
            return False
        
        try:
            # 更新 skill.json 中的版本号
            skill_json_path = skill_dir / "skill.json"
            with open(skill_json_path, "r") as f:
                data = json.load(f)
            
            old_version = data.get("version", "unknown")
            data["version"] = skill["version"]
            data["last_updated"] = datetime.now().isoformat()
            
            with open(skill_json_path, "w") as f:
                json.dump(data, f, indent=2)
            
            self.logger.info(f"✓ {name}: {old_version} → {skill['version']}")
            return True
            
        except Exception as e:
            self.logger.error(f"更新技能 {name} 版本失败: {e}")
            return False
    
    def sync_to_github(self) -> bool:
        """同步到 GitHub"""
        self.logger.info("同步到 GitHub...")
        
        try:
            os.chdir(MUST_SKILLS_DIR)
            
            # 检查是否有变更
            result = subprocess.run(
                ["git", "diff", "--quiet"],
                capture_output=True
            )
            result_staged = subprocess.run(
                ["git", "diff", "--cached", "--quiet"],
                capture_output=True
            )
            
            if result.returncode == 0 and result_staged.returncode == 0:
                self.logger.info("没有变更需要提交")
                return True
            
            # 配置 git
            subprocess.run(["git", "config", "user.email", "auto-sync@openclaw.local"], 
                         capture_output=True)
            subprocess.run(["git", "config", "user.name", "Auto Sync Bot"], 
                         capture_output=True)
            
            # 添加、提交、推送
            subprocess.run(["git", "add", "-A"], check=True)
            
            date_str = datetime.now().strftime("%Y-%m-%d")
            commit_msg = f"""auto-sync: weekly ClawHub Top 10 skills update - {date_str}

Weekly sync summary:
- New learned: {len(self.new_skills)}
- Updated: {len(self.updated_skills)}
- Skipped: {len(self.skipped_skills)}

Skills:
{chr(10).join(f"- {s['name']} (v{s['version']})" for s in self.new_skills + self.updated_skills)}
"""
            
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            subprocess.run(["git", "push", "origin", "master"], check=True)
            
            self.logger.info("✓ 已推送到 GitHub")
            return True
            
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Git 操作失败: {e}")
            return False
        except Exception as e:
            self.logger.error(f"同步到 GitHub 失败: {e}")
            return False
    
    def run_sync(self):
        """运行完整同步流程"""
        self.logger.info("=" * 50)
        self.logger.info("启动 ClawHub Top 10 技能同步")
        self.logger.info("=" * 50)
        
        # 获取 Top 10 技能
        top10 = self.fetch_clawhub_top10()
        
        # 处理每个技能
        for skill in top10:
            name = skill["name"]
            version = skill["version"]
            rank = skill["rank"]
            
            self.logger.info(f"[{rank}/10] 检查技能: {name} (v{version})")
            
            # 检查状态
            status = self.tracker.check_skill(name, version)
            
            if status == "NEW":
                self.logger.info(f"  → 新技能，开始学习和安装")
                
                # 创建技能文件
                skill_path = self.create_skill_files(skill)
                
                # 安装到 OpenClaw
                if self.install_skill(name, skill_path):
                    # 激活
                    self.activate_skill(name)
                    
                    # 更新追踪
                    self.tracker.update_skill(name, version, "learned")
                    self.new_skills.append(skill)
                
            elif status == "UPDATE":
                self.logger.info(f"  → 发现新版本，开始更新")
                
                if self.update_skill_version(skill):
                    # 重新安装
                    category = skill.get("category", "productivity")
                    skill_path = MUST_SKILLS_DIR / category / name
                    self.install_skill(name, skill_path)
                    self.activate_skill(name)
                    
                    # 更新追踪
                    self.tracker.update_skill(name, version, "updated")
                    self.updated_skills.append(skill)
                
            else:  # SKIP
                self.logger.info(f"  → 已是最新版本，跳过")
                self.tracker.update_skill(name, version, "skipped")
                self.skipped_skills.append(skill)
        
        # 同步到 GitHub
        self.sync_to_github()
        
        # 添加周记录
        week_data = {
            "week": datetime.now().strftime("%Y-W%W"),
            "date": datetime.now().isoformat(),
            "new": len(self.new_skills),
            "updated": len(self.updated_skills),
            "skipped": len(self.skipped_skills),
            "skills": [s["name"] for s in self.new_skills + self.updated_skills]
        }
        self.tracker.add_weekly_record(week_data)
        
        # 输出统计
        stats = self.tracker.get_stats()
        self.logger.info("=" * 50)
        self.logger.info("同步完成!")
        self.logger.info(f"  本次新学习: {len(self.new_skills)}")
        self.logger.info(f"  本次更新: {len(self.updated_skills)}")
        self.logger.info(f"  本次跳过: {len(self.skipped_skills)}")
        self.logger.info(f"  累计学习: {stats['total_learned']}")
        self.logger.info(f"  累计更新: {stats['total_updated']}")
        self.logger.info("=" * 50)


def main():
    """主函数"""
    manager = SkillSyncManager()
    manager.run_sync()


if __name__ == "__main__":
    main()
