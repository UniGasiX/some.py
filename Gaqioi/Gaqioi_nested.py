# 有约定的占位符 ABRACADABRA
# 这里用的是四个空格作为缩进，
# 最后处理时会把每一组四个空格改成一个制表符并使用转义字符，
# >>需要注意<<。

try:
    from MyQR import myqr
    print('生成路径：'+myqr.run('ABRACADABRA',save_name=input('- by UniGasiX -\n请指定输出图片文件名（不含扩展名）：')+'.png',level='Q')[2])
except ModuleNotFoundError:
    print('错误！这段程序需要使用MyQR库。\n可以尝试命令 pip3 install myqr 安装MyQR库。')
