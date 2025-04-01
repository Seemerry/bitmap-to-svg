# Bitmap to SVG Converter

一个将位图图像（.png, .jpg, .jpeg）转换为 SVG 矢量图的小工具，适用于黑白线条图、LOGO、简洁图标等图像的轮廓提取。

支持功能：
- 自动将图片轮廓转为 SVG 折线图形
- 输出 SVG 文件到指定目录
- 自动复制生成的 SVG 源代码到系统剪贴板，便于快速粘贴使用
- 支持批处理（目前默认只处理一张图）

---

## 🗂 项目结构

```
project-root/
│
├── src/                  # 主程序源码
│   └── bitmap_to_svg.py
│
├── src_img/              # 原始图片输入目录（你要处理的图片放这里）
│   └── ChatGPT.png
│
├── svg_out/              # 生成的 SVG 输出目录
│
├── svg_env/              # Python 虚拟环境（建议使用）
│
└── requirements.txt      # 项目依赖文件
```



---

## ⚙️ 环境准备

建议使用 Python 3.9 及以上版本。

### 1. 创建虚拟环境（可选但推荐）

```
python -m venv svg_env
```

------------

### 2. 激活虚拟环境

#### Window

```
svg_env\Scripts\activate
```

#### macOS / Linux

```
source svg_env/bin/activate
```

------------

### 3. 安装依赖

```
pip install -r requirements.txt
```

## ▶️ 使用方法

1. 将图片放入 src_img/ 文件夹中

支持 .png、.jpg、.jpeg 格式，推荐黑白线条图或 Logo。

2. 运行转换脚本

```
python src/bitmap_to_svg.py
```

运行成功后会：
	•	在 svg_out/ 中生成同名 .svg 文件
	•	自动将 SVG 源代码复制到你的剪贴板（你可以直接 Ctrl+V 粘贴）

------------

### ✅ 示例输出

处理 src_img/ChatGPT.png 后将生成：
	•	svg_out/ChatGPT.svg 文件
	•	控制台提示：

🔄 处理图像: ChatGPT.png
✅ 已保存 SVG: svg_out/ChatGPT.svg
📋 SVG 源代码已复制到剪贴板！你现在可以直接粘贴啦~

------------

## 🧠 注意事项

​	•	目前只处理一张图（可自行去掉 break 以支持批量处理）
​	•	图像应尽量清晰、对比明显，推荐使用黑白图或高对比 Logo
​	•	彩色图处理会被简化为黑白轮廓（后续可支持颜色提取）

------------

📌 TODO（可选功能扩展）
	•	支持彩色区域近似填充
	•	批量处理所有图片
	•	增加命令行参数（如 --threshold、--copy 等）
	•	加 GUI 或网页上传界面

------------

🧑‍💻 作者

本工具由Seemerry开发，使用了：
	•	OpenCV（图像处理）
	•	scikit-image（轮廓提取）
	•	svgwrite（SVG 生成）
	•	pyperclip（剪贴板操作）

欢迎自由扩展或改造成自己的工具！

