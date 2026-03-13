# Notion

Notion API 集成，帮助用户轻松创建、管理 Notion 页面、数据库和内容块，实现工作流程自动化。

## 配置

```bash
export NOTION_API_KEY="secret_xxx"
export NOTION_VERSION="2022-06-28"
```

获取 API Key:
1. 访问 https://www.notion.so/my-integrations
2. 创建新集成
3. 复制 Internal Integration Token
4. 将集成分享给需要访问的页面

## 功能

### 1. 页面管理
- 创建页面
- 更新页面
- 获取页面内容
- 归档/删除页面

### 2. 数据库操作
- 查询数据库
- 创建数据库条目
- 更新数据库属性
- 筛选和排序

### 3. 内容块
- 添加文本块
- 插入代码块
- 嵌入媒体
- 创建待办列表

## 使用示例

```bash
# 创建页面
notion page create --parent "xxx" --title "新页面" --content "内容"

# 查询数据库
notion database query --id "xxx" --filter '{"property":"Status","select":{"equals":"Done"}}'

# 创建数据库条目
notion database insert --id "xxx" --properties '{"Name":{"title":[{"text":{"content":"任务1"}}]}}'

# 获取页面内容
notion page get --id "xxx"
```

## 常见用例

- 自动同步任务到 Notion
- 创建每日/每周报告
- 管理项目进度
- 构建知识库
- 团队协作文档

## 数据类型支持

- Title, Rich Text
- Number, Select, Multi-select
- Date, Checkbox
- URL, Email, Phone
- Files & Media
- Relation, Rollup
- Formula
