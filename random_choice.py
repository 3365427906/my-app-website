import random
import os
from datetime import datetime

# 配置
choices = ['A', 'B']
output_dir = 'data/choices'

# 创建目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 生成文件名（格式：2023-10-05.txt）
today = datetime.now().strftime('%Y-%m-%d')
filename = os.path.join(output_dir, f'{today}.txt')

# 随机选择并写入文件
selected = random.choice(choices)
with open(filename, 'w') as f:
    f.write(selected)

print(f'今日选择：{selected}，已保存到 {filename}')
