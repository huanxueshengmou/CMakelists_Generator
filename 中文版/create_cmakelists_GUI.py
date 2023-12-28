import os
import tkinter as tk
from tkinter import filedialog, simpledialog

def create_cmakelists(directory, levels):
    # 检查当前目录是否存在 .cpp 或 .c 文件
    contains_cpp_files = any(file.endswith((
    '.cpp', '.cxx', '.cc', '.c++', '.C','.c',   # C++
    '.c',                                       # C
    '.f', '.for', '.f90',                       # Fortran
    '.java',                                    # Java
    '.cs',                                      # C#
    '.py',                                      # Python
    # 可以根据需要继续添加其他编程语言的扩展名
                                            )) for file in os.listdir(directory))

    # 如果目录中有 .cpp 或 .c 文件且 CMakeLists.txt 不存在，则创建它
    if contains_cpp_files and not os.path.isfile(os.path.join(directory, 'CMakeLists.txt')):
        with open(os.path.join(directory, 'CMakeLists.txt'), 'w', encoding='utf-8') as cmakelists:
            cmakelists.write('cmake_minimum_required(VERSION 3.10)\n\n# 添加你的项目设置\n')
        print(f'在 {directory} 中创建了 CMakeLists.txt')
    
    # 如果 levels 为 0，代表这是我们需要检查的最后一个目录
    if levels == 0:
        return

    # 递归地在子目录中创建 CMakeLists.txt，如果他们包含 .cpp 或 .c 文件
    for dirpath, dirnames, filenames in os.walk(directory):
        # 如果我们达到了指定的层数深度，则跳过子目录
        if os.path.relpath(dirpath, directory).count(os.sep) >= levels:
            continue
        for subdir in dirnames:
            create_cmakelists(os.path.join(dirpath, subdir), levels - 1)

def gui_create_cmakelists():
    # 使用文件对话框选择目录
    directory = filedialog.askdirectory()
    # 确保用户没有取消目录选择
    if directory:
        # 用户输入要遍历的层数（0 表示只检查当前目录）
        levels = simpledialog.askinteger("输入层数", "输入要遍历的层数（0表示只检查当前目录）:")
        # 确保用户输入了一个数字
        if levels is not None:
            create_cmakelists(directory, levels)

# 创建主窗口
root = tk.Tk()
root.title("CMakeLists 创建器")

# 创建一个标签和按钮来选择目录并执行函数
label = tk.Label(root, text="选择一个目录并输入层数", padx=10, pady=10)
label.pack()

create_button = tk.Button(root, text="创建 CMakeLists", command=gui_create_cmakelists, padx=20, pady=5)
create_button.pack()

# 执行事件循环
root.mainloop()