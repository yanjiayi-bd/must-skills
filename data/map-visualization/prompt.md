# Map Visualization

只需输入地理范围以及对应数据，即可得到数据可视化地图。数据支持搜索、自然语言描述、JSON、Excel 等格式。

## 功能

### 1. 地图类型
- 热力图 (Heatmap)
- 区域填充图 (Choropleth)
- 点标记图 (Scatter)
- 路径图 (Route)
- 3D 地图

### 2. 数据格式支持
- CSV / Excel
- JSON / GeoJSON
- 自然语言描述
- 数据库查询结果

### 3. 交互功能
- 缩放和平移
- 悬停提示
- 点击详情
- 图例筛选

## 使用示例

```bash
# 基本用法
map-viz "显示中国各省份GDP分布"

# 从文件读取数据
map-viz --data data.csv --type choropleth --region china

# 热力图
map-viz --data locations.json --type heatmap --center " Beijing"

# 自定义样式
map-viz --data sales.xlsx --theme dark --color-scheme blues

# 导出地图
map-viz --data input.json --output map.png --width 1920 --height 1080
```

## 数据格式示例

**CSV:**
```csv
province,value
北京,100
上海,95
广东,88
```

**JSON:**
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "name": "北京", "value": 100 },
      "geometry": { "type": "Point", "coordinates": [116.4, 39.9] }
    }
  ]
}
```

## 应用场景

- 销售数据地域分布
- 人口密度分析
- 疫情传播可视化
- 物流路径规划
- 环境监测数据展示

## 支持的地图

- 世界地图
- 中国地图（省/市/区）
- 美国地图（州/县）
- 欧洲地图
- 自定义 GeoJSON
