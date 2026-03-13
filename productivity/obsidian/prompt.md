# Obsidian

管理 Obsidian 笔记库，处理纯 Markdown 格式的笔记，通过 obsidian-cli 实现自动化操作。

## 安装

```bash
# 安装 obsidian-cli
npm install -g @thombruce/obsidian-cli

# 或使用 obsidian-export
pip install obsidian-exporter
```

## 配置

```bash
# 设置 vault 路径
export OBSIDIAN_VAULT_PATH="/path/to/your/vault"
```

## 功能

### 1. 笔记管理
- 创建新笔记
- 搜索笔记
- 更新内容
- 移动/删除笔记

### 2. 链接与关系
- 创建双向链接
- 查看反向链接
- 图谱分析
- 标签管理

### 3. 内容操作
- 批量重命名
- 模板应用
- 元数据管理
- 附件整理

## 使用示例

```bash
# 创建笔记
obsidian-cli create "项目/新想法" --content "## 想法\n\n内容"

# 搜索笔记
obsidian-cli search "关键词"

# 获取笔记内容
obsidian-cli read "项目/新想法"

# 更新笔记
obsidian-cli update "项目/新想法" --append "\n\n新内容"

# 创建链接
obsidian-cli link "笔记A" "笔记B"

# 列出标签
obsidian-cli tags --list
```

## 与 Zettelkasten 结合

```bash
# 创建原子笔记
obsidian-cli create "Zettelkasten/$(date +%Y%m%d%H%M%S)" --template atomic

# 链接相关笔记
obsidian-cli backlinks "当前笔记"
```

## 常见工作流

1. **每日笔记**: 自动创建每日日记
2. **文献管理**: 整理阅读笔记和引用
3. **项目管理**: 追踪任务和进度
4. **知识图谱**: 构建概念关系网络
