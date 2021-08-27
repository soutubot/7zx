# 批量解压(子)目录所有压缩文件(zip\rar\7z\分卷)
## 详细流程  
先检测是否符号命名规则的压缩文件  
再按原压缩文件目录结构的基础上  
批量解压到新建的{文件夹路径-OK}目录里  
  
已适配的压缩文件命名规则
`*.zip` `*.rar` `*.7z` `*.part0*.rar` `*.7z.0*`  
PS.未做解压删除

## 更新记录
- 支持指定密码 `python3 7zx.py 路径 密码`  
暂不支持多重/不同/奇怪特殊符号的密码

## 环境
- `python 3.7+`
- `7zip`  
-Linux `apt-get install p7zip p7zip-full`  
-Window 环境变量添加 `C:\Program Files\7-Zip`  

## 用法
```
python3 7zx.py 文件夹路径(结尾不能有斜杠) 密码
```
--列子
```
python3 7zx.py D:\test\RAR
python3 7zx.py D:\test\RAR password
```
