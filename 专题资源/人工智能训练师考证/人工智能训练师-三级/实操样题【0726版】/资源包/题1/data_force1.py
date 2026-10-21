import cv2
import os
import random
import numpy as np

# 读取数据集文件夹路径
data_path = "data_force"

# 扩充倍数
expand_factor = <1>

# 随机选择30%的图片进行顺时针旋转45度
file_list = os.listdir(data_path)
rotate_amount = round(len(file_list) * <2>)

# 对30%的图片进行顺时针旋转45度
rotate_list = random.sample(file_list, rotate_amount)
for file in rotate_list:
    # 获取当前图片的完整路径
    path = os.path.join(data_path, file)

    # 读取图片
    with open(path, 'rb') as f:
        data = np.frombuffer(f.read(), dtype=np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)

    # 图片顺时针旋转45度
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), <3>, 1)
    img = cv2.warpAffine(img, M, (cols, rows))

    # 保存图片到原文件路径中
    success, encoded_image = cv2.imencode(os.path.splitext(file)[1], img)
    with open(path, 'wb') as f:
        f.write(encoded_image)

# 对所有图片进行扩充
file_list = os.listdir(data_path)
for file in file_list:
    # 获取当前图片的完整路径
    path = os.path.join(data_path, file)

    # 读取图片
    with open(path, 'rb') as f:
        data = np.frombuffer(f.read(), dtype=np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)

    # 对图片进行扩充
    for i in range(expand_factor):
        # 将文件名分割成文件名（不含路径）和扩展名
        filename, ext = os.path.splitext(file)

        # 生成新的文件名
        new_filename = filename + "_" + str(i+1) + ext

        # 构建新的文件路径
        new_path = os.path.join("1-2数据增强", <4>)

        # 图片逆时针旋转45度
        rows, cols = img.shape[:2]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
        img_rotated = cv2.warpAffine(img, M, (cols, rows))

        # 保存图片到新的文件路径中
        success, encoded_image = cv2.imencode(ext, img_rotated)
        with open(new_path, 'wb') as f:
            f.write(encoded_image)