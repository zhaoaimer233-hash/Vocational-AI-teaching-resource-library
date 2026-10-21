import <1>
import shutil
from PIL import Image

# 设置数据文件夹路径和目标文件夹路径
data_folder = "data/"
target_folder = <2>

# 获取所有文件名
file_names = os.<3>(data_folder)

# 遍历所有文件并检查是否为RGB格式和JPG格式
for file_name in file_names:
    file_path = os.path.join(data_folder, file_name)
    img = Image.open(file_path)
    if img.mode != 'RGB' or os.path.splitext(file_name)[1] != '.jpg':
        # 如果不是RGB格式或JPG格式，则将文件移动到目标文件夹
        try:
            img.close()  # 关闭Image对象
            shutil.move(file_path, target_folder)
            print(f"Moved {file_name} to {target_folder}")
        except Exception as e:
            print(f"Failed to move {file_name}: {e}")
