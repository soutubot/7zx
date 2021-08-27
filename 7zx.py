# -*- codeing = utf-8 -*-
# @Time : 2021/8/27 1:28
# @Autor : Soutubot
# @File : 7zx.py
# @Software : PyCharm

import os
import platform
from pathlib import Path
from sys import argv, exit

compressed_file = []

def un7z(file, folder_name, folder_rename):
    files_path = file
    if platform.system().lower() == 'windows': #win
        files_path = f'"{str(files_path)}"' #压缩文件路径
        files_name = str(file).split('\\')[-1] #文件名
        files_to_path = files_path.replace(folder_name, folder_rename).replace(files_name,'') #解压到OK目录路径
    elif platform.system().lower() == 'linux': #Linux
        files_path = f"'{str(files_path)}'" #压缩文件路径
        files_name = str(file).split('/')[-1] #文件名
        files_to_path = files_path.replace(folder_name, folder_rename).replace(files_name, '') #解压到OK目录路径

    cmd = f'7z x -pfaust {files_path} -o{files_to_path}' #7z解压命令
    #print(cmd)
    cmd_run = os.system(cmd)
    print(cmd_run)
    print('---------')


if __name__ == "__main__":
    if len(argv) == 1: #判断参数
        print(f'Usage: {argv[0]} DIR')
        exit()
    if len(argv) == 2: #判断参数
        for file in Path(argv[1]).glob("**/*"): #遍历所有子目录子文件
            if os.path.isfile(file): #判断是否为文件
                if '.rar' in str(file): #判断rar和第一个分卷文件
                    if '.part01.rar' in str(file) or '.part1.rar' in str(file):
                        compressed_file.append(file)
                    elif '.part' not in str(file):
                        compressed_file.append(file)
                elif '.7z' in str(file): #判断7z和第一个分卷文件
                    if '.7z.001' in str(file):
                        compressed_file.append(file)
                    elif '.7z.0' not in str(file):
                        compressed_file.append(file)
                elif '.zip' in str(file): #判断zip文件
                    compressed_file.append(file)

        #重命名OK名
        if platform.system().lower() == 'windows':  # win
            folder_name = argv[1].split('\\')[-1]
            folder_rename = f'{folder_name}-OK'
            #print('win')
        elif platform.system().lower() == 'linux':  # Linux
            folder_name = argv[1].split('/')[-1]
            folder_rename = f'{folder_name}-OK'
            #print('linux')

        if not folder_name: #判断替换文件名否有出错(空)
            print(f'目录结尾不能有斜杠')
            exit()

        for files in compressed_file: #开始批量解压
            un7z(files, folder_name, folder_rename)
            #print(files, folder_name, folder_rename)
