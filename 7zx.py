# -*- codeing = utf-8 -*-
# @Time : 2021/8/27 1:28
# @Autor : Soutubot
# @File : 7zx.py
# @Software : PyCharm
import re
import os
import platform
from pathlib import Path
from sys import argv, exit

compressed_file_all = []
compressed_file_not = []
compressed_file_one = []
compressed_file_part = []

def del_compressed(files_name_2):
    for file_part in compressed_file_all:
        if files_name_2 in str(file_part):
            if os.path.exists(file_part):
                os.remove(file_part)
                print(f'已删除-{file_part}')
            else:
                print(f'删除失败-{file_part}')

def un7z(file, folder_name, folder_rename, password, type):
    files_path = file
    if platform.system().lower() == 'windows' :  #win
        files_path = f'"{str(files_path)}"' #压缩文件路径
        files_name = str(file).split('\\')[-1] #文件名
        files_to_path = files_path.replace(folder_name, folder_rename).replace(files_name,'') #解压到OK目录路径
    elif platform.system().lower() == 'linux': #Linux
        if "'" in str(file):
            files_path = f'"{str(files_path)}"'  # 压缩文件路径
            files_name = str(file).split('/')[-1]  # 文件名
            files_to_path = files_path.replace(folder_name, folder_rename).replace(files_name, '')  # 解压到OK目录路径
        else:
            files_path = f"'{str(files_path)}'" #压缩文件路径
            files_name = str(file).split('/')[-1] #文件名
            files_to_path = files_path.replace(folder_name, folder_rename).replace(files_name, '') #解压到OK目录路径

    if not password : #判断是否有指定密码
        cmd = f'7z x {files_path} -o{files_to_path}'  # 7z解压命令
    else:
        cmd = f'7z x -p{password} {files_path} -o{files_to_path}' #7z解压命令
    #print(cmd)
    cmd_run = os.system(cmd)
    print(cmd_run)
    print('---------')

    if del_compressed_switch == 'del=ON':
        if type == 'part' :
            if re.search('.*.part1.rar$', str(file)):
                files_name_2 = re.sub(r'1.rar$', r'', str(file))
                del_compressed(files_name_2)
            elif re.search('.*.part01.rar$', str(file)):
                files_name_2 = re.sub(r'01.rar$', r'', str(file))
                del_compressed(files_name_2)
            elif re.search('.*.7z.[0-9][0-9][0-9]$', str(file)):
                files_name_2 = re.sub(r'.001$', r'', str(file))
                del_compressed(files_name_2)
        elif type == 'one' :
            if os.path.exists(file):
                os.remove(file)
                print(f'已删除-{file}')
            else:
                print(f'删除失败-{file}')

if __name__ == "__main__":
    print(argv)
    if len(argv) == 1: #判断参数
        print(f'Usage: {argv[0]} DIR')
        exit()
    if len(argv) == 2:
        password = ''
    if len(argv) == 3:
        if argv[2] == 'del=ON':
            print('OK')
            password = ''
            del_compressed_switch = argv[2]
        else:
            password = argv[2]
            del_compressed_switch = ''
    if len(argv) == 4:
        password = argv[2]
        del_compressed_switch = argv[3]
    if 5 > len(argv) >= 2: #判断参数

        #重命名OK名
        if platform.system().lower() == 'windows':  # win
            folder_name = argv[1].split('\\')[-1]
            folder_rename = f'{folder_name}-OK'
        elif platform.system().lower() == 'linux':  # Linux
            folder_name = argv[1].split('/')[-1]
            folder_rename = f'{folder_name}-OK'

        if not folder_name: #判断替换文件名否有出错(空)
            print(f'目录结尾不能有斜杠')
            exit()

        for file in Path(argv[1]).glob("**/*"): #遍历所有子目录子文件
            if os.path.isfile(file): #判断是否为文件

                if re.search('.*.rar$', str(file)):
                    compressed_file_all.append(file)
                    if re.search('.*.part01.rar$', str(file)) or re.search('.*.part1.rar$', str(file)):
                        compressed_file_part.append(file)
                    if not re.search('.*.part[0-9][0-9]?.rar$', str(file)):
                        compressed_file_one.append(file)

                elif re.search('.*.zip$', str(file)):
                    compressed_file_all.append(file)
                    compressed_file_one.append(file)

                elif re.search('.*.7z$', str(file)):
                    compressed_file_all.append(file)
                    compressed_file_one.append(file)

                elif re.search('.*.7z.[0-9][0-9][0-9]$', str(file)):
                    compressed_file_all.append(file)
                    if re.search('.*.7z.001$', str(file)):
                        compressed_file_part.append(file)

                else:
                    compressed_file_not.append(file)

        for files in compressed_file_part: #开始批量解压
            un7z(files, folder_name, folder_rename, password, 'part')

        for files in compressed_file_one: #开始批量解压
            un7z(files, folder_name, folder_rename, password, 'one')
