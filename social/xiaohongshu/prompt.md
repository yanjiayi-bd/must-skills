# 小红书 Automation

小红书内容运营自动化工具，通过 Python 客户端实现。

## 功能

### 1. 内容发布
- 发布图文笔记
- 发布视频内容
- 批量发布管理
- 定时发布

### 2. 数据分析
- 搜索笔记趋势
- 分析帖子评论
- 用户互动统计
- 热门话题追踪

### 3. 用户管理
- 获取用户资料
- 关注/取消关注
- 粉丝互动
- 私信管理

### 4. 内容发现
- 首页内容获取
- 热门内容抓取
- 关键词搜索
- 话题标签分析

## 使用示例

```bash
# 发布图文笔记
xiaohongshu post --image "cover.jpg" --title "标题" --content "内容"

# 搜索热门话题
xiaohongshu search --keyword "AI工具" --limit 50

# 分析评论
xiaohongshu analyze --post-id "xxx" --comments

# 获取用户数据
xiaohongshu user --username "xxx" --profile
```

## 注意事项

- 需要小红书账号授权
- 遵守平台规则，避免过度操作
- 注意频率限制
