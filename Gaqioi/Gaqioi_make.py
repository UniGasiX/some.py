# 从 Gaqioi_shell.py 和 Gaqioi_nested.py
# 合成并处理出可以被 MyQR 库转换出 QR Code 图片的代码。

shell_str = ""
nested_str = ""
nested_parts = []
gaqioi_str = ""

# 读取两个文件的代码，并删除空行和以字符#开始的注释行

with open("Gaqioi_shell.py", "r", encoding="utf-8") as f:
    lines = []
    for line in f.readlines():
        if len(line) > 0 and line != "\n" and not line.startswith("#"):
            lines.append(line)
    shell_str = "".join(lines)


with open("Gaqioi_nested.py", "r", encoding="utf-8") as f:
    lines = []
    for line in f.readlines():
        if len(line) > 0 and line != "\n" and not line.startswith("#"):
            lines.append(line)
    nested_str = "".join(lines)

# 处理nested

# myqr 源码里写的允许的字符
allowed = r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ··,.:;+-*/\~!@#$%^&`'=<>[]()?_{}|"
# 转义特殊字符
nested_str = nested_str.replace("\\", "\\\\").replace(
    "\n", "\\n").replace("'", "\\'")
# 这里再做一点处理，因为微信扫描二维码结果会把连在一起的几个空格省略为一个，
# 而代码又用了四个空格作为缩进，而许多人确实会用微信扫二维码
nested_str = nested_str.replace("    ", "\\t")
# 将所有不允许的字符转成unicode转义字符形式
nested_str = "".join([(('\\u'+format(ord(c), 'x').zfill(4))
                       if c not in allowed else c) for c in nested_str])
# 把nested按照约定的占位符拆开
nested_parts = nested_str.split("ABRACADABRA")

# 处理shell
shell_str = shell_str.replace("\n", "")

# 合成最终代码

# 在约定的占位符处插入nested
gaqioi_str = shell_str.replace("ABRACADABRA1", nested_parts[0]).replace(
    "ABRACADABRA2", nested_parts[1]) + " # Copyright (C) 2019 UniGasiX | Licensed under GNU GPLv3.0 | ATTENTION!!!: The MyQR package is needed. You may try ** pip3 install myqr ** to install."
with open("Gaqioi.py", "w") as f:
    f.write(gaqioi_str)
