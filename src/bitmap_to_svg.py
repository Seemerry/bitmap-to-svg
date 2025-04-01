# 导入必要的库
import cv2  # OpenCV库，用于图像处理
import os  # 用于文件和目录操作
from skimage import measure  # scikit-image中的measure模块，用于轮廓检测
import svgwrite  # 用于创建和操作SVG文件
import pyperclip  # 用于操作系统剪贴板

# 输入输出目录
INPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'src_img')  # 源图像目录，相对于脚本位置
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'svg_out')  # SVG输出目录，相对于脚本位置
SUPPORTED_EXTENSIONS = ['.png', '.jpg', '.jpeg']  # 程序支持处理的图像格式列表

def bitmap_to_svg(image_path, svg_path, threshold=128):
    """
    将位图转换为SVG矢量图
    
    参数:
        image_path (str): 输入图像的路径
        svg_path (str): 输出SVG文件的路径
        threshold (int): 二值化阈值，默认为128
    """
    # 以灰度模式读取图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"❌ 无法读取图像: {image_path}")
        return

    # 对图像进行二值化处理，THRESH_BINARY_INV表示反转二值化结果（黑白颠倒）
    _, binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
    # 使用scikit-image的find_contours函数检测轮廓，0.5是轮廓级别阈值
    contours = measure.find_contours(binary, 0.5)

    # 创建SVG绘图对象，设置尺寸与原图相同
    dwg = svgwrite.Drawing(size=(image.shape[1], image.shape[0]))
    # 遍历所有检测到的轮廓
    for contour in contours:
        # 将轮廓点坐标转换为整数，并交换x和y坐标（因为find_contours返回的是(row, col)格式）
        points = [(int(p[1]), int(p[0])) for p in contour]
        # 将轮廓添加到SVG中作为折线，不填充，黑色描边，线宽为1
        dwg.add(dwg.polyline(points, fill='none', stroke='black', stroke_width=1))

    # 保存SVG文件到指定路径
    dwg.saveas(svg_path)
    print(f"\n✅ 已保存 SVG: {svg_path}")

    # 获取SVG源代码（XML格式）
    svg_code = dwg.tostring()

    # 将SVG源代码复制到系统剪贴板，方便用户直接粘贴使用
    pyperclip.copy(svg_code)
    print("📋 SVG 源代码已复制到剪贴板！你现在可以直接粘贴啦~")

def process_all_images():
    """
    处理输入目录中的所有支持格式的图像，将它们转换为SVG并保存到输出目录
    """
    # 如果输出目录不存在，则创建它
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(INPUT_DIR):
        # 分离文件名和扩展名
        name, ext = os.path.splitext(filename)
        # 检查文件扩展名是否在支持的格式列表中
        if ext.lower() in SUPPORTED_EXTENSIONS:
            # 构建完整的输入和输出文件路径
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"{name}.svg")
            print(f"\n🔄 处理图像: {filename}")
            # 调用转换函数处理图像
            bitmap_to_svg(input_path, output_path)
            break  # ⚠️ 只处理一张图像并复制到剪贴板（防止多个图像覆盖剪贴板）

# 程序入口点
if __name__ == "__main__":
    process_all_images()  # 调用函数处理所有图像