# Polymarket

Polymarket 预测市场查询工具，实时查看赔率、热门趋势，搜索事件，追踪价格与动向。

## 功能

### 1. 市场概览
- 热门市场查看
- 最新事件追踪
- 交易量排行
- 趋势分析

### 2. 事件搜索
- 关键词搜索
- 分类筛选
- 即将到期事件
- 高流动性市场

### 3. 价格追踪
- 实时赔率
- 价格历史
- 交易量变化
- 市场深度

### 4. 关注列表
- 自定义关注
- 价格提醒
- 结算日历
- 持仓跟踪

## 使用

```bash
# 查看热门市场
polymarket trending

# 搜索事件
polymarket search "美国大选"
polymarket search "BTC价格" --category crypto

# 获取市场详情
polymarket market "event-id"

# 查看赔率历史
polymarket odds "event-id" --history 7d

# 关注列表
polymarket watchlist --add "event-id"
polymarket watchlist --list

# 结算日历
polymarket calendar --upcoming

# 分类浏览
polymarket browse --category politics
polymarket browse --category crypto
polymarket browse --category sports
```

## 输出示例

```markdown
# Polymarket 市场数据

## 热门: 美国大选 2024
- YES: 0.62 (+2.3%)
- NO: 0.38 (-1.5%)
- 交易量: $2.3M
- 结算: 2024-11-05

## 趋势分析
过去24小时：
- YES 买压增加
- 大额交易: 3笔
- 社交媒体情绪: 中性偏多
```

## 市场分类

- 🏛️ Politics (政治)
- 💰 Crypto (加密货币)
- 🏈 Sports (体育)
- 🎬 Entertainment (娱乐)
- 🌍 World (国际)
- 💻 Tech (科技)

## 免责声明

预测市场涉及金融风险，请谨慎参与。本工具仅供信息查询，不构成投资建议。
