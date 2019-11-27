# 有约定的占位符 ABRACADABRA

try:
    from MyQR import myqr
    name = input("Gaqioi\nCopyright (C) 2019 UniGasiX\nLicensed under GPL v3.0\n请指定输出图片的文件名（不含扩展名）：")
    myqr.run('ABRACADABRA', save_name=name+".png")
except ModuleNotFoundError:
    print("错误！这段程序需要MyQR库。\n可以尝试命令 pip3 install myqr 安装MyQR库。")
