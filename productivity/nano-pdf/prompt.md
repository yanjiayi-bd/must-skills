# Nano PDF

轻量级 PDF 编辑 CLI 工具，支持通过自然语言指令轻松编辑 PDF 文件。

## 功能

### 1. 页面操作
- 合并多个 PDF
- 拆分 PDF
- 旋转页面
- 删除页面
- 重新排序

### 2. 内容编辑
- 添加文本
- 插入图片
- 添加水印
- 高亮标注

### 3. 格式转换
- PDF 转图片
- 图片转 PDF
- PDF 压缩
- 优化文件大小

### 4. 元数据管理
- 读取/修改标题
- 设置作者
- 添加关键词
- 查看 PDF 信息

## 使用示例

```bash
# 合并 PDF
nano-pdf merge file1.pdf file2.pdf --output merged.pdf

# 拆分 PDF
nano-pdf split input.pdf --pages "1-5,10-15" --output part.pdf

# 压缩 PDF
nano-pdf compress input.pdf --quality medium --output compressed.pdf

# 添加水印
nano-pdf watermark input.pdf --text "CONFIDENTIAL" --output watermarked.pdf

# PDF 转图片
nano-pdf convert input.pdf --format png --output ./pages/

# 旋转页面
nano-pdf rotate input.pdf --pages "2,4" --angle 90 --output rotated.pdf

# 删除页面
nano-pdf remove input.pdf --pages "3,5-7" --output cleaned.pdf
```

## 自然语言操作

```bash
# 使用自然语言描述操作
nano-pdf "把第一页和最后一页合并成新文件"
nano-pdf "压缩这个PDF到5MB以内"
nano-pdf "给所有页面加上机密水印"
```

## 批量处理

```bash
# 批量压缩
nano-pdf batch compress *.pdf --quality low

# 批量合并
nano-pdf batch merge ./docs/ --output combined.pdf
```

## 依赖

- Python 3.8+
- PyPDF2 / pikepdf
- Pillow (图片处理)
