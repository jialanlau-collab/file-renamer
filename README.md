# file-renamer

一个简单的命令行批量重命名工具，支持替换文字、加前缀、加后缀、按序号重命名四种模式。
默认只预览，确认无误后加 `--apply` 才真正改名，安全不会误操作。

## 准备

需要电脑装了 Python 3（[python.org](https://www.python.org) 下载安装即可，安装时勾选 "Add Python to PATH"）。

## 用法

先进入脚本所在文件夹，把 `./你的文件夹` 换成要处理的文件夹路径：

### 1. 替换文件名里的文字
把所有文件名里的 `IMG_` 换成 `旅行_`：
```bash
python rename.py ./照片 --mode replace --old "IMG_" --new "旅行_"
```

### 2. 批量加前缀
所有文件名前面加 `2026_`：
```bash
python rename.py ./照片 --mode prefix --prefix "2026_"
```

### 3. 批量加后缀
所有文件名后面加 `_终稿`（在扩展名之前）：
```bash
python rename.py ./照片 --mode suffix --suffix "_终稿"
```

### 4. 按序号重命名
把文件统一改成 `file_001`、`file_002`……（保留原扩展名）：
```bash
python rename.py ./照片 --mode number --start 1
```

## 安全机制

- 不加 `--apply` 时只打印预览，不改动任何文件
- 如果目标文件名已存在，自动跳过避免覆盖
- 只处理文件夹下的直接文件，不递归子文件夹

确认预览没问题后，在命令最后加 `--apply` 真正执行：
```bash
python rename.py ./照片 --mode prefix --prefix "2026_" --apply
```
