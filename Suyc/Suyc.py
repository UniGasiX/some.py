# Copyright (C) 2019 UniGasiX
# Lisenced under GPL v3.0
#
# Suyc - Speed up your conversion
# version 0.1

from typing import *
from datetime import datetime, timedelta
import random
import re

option = "131"  # 默认设置
opt_reg = re.compile("^([1-4])([1-4])([12])$")
bnf = {"1": ("二进制", "b"), "2": ("八进制", "o"), "3": ("十进制", "d"), "4": ("十六进制", "X")}
rnr = {"1": ("0~15", (0, 15)), "2": ("16~255", (16, 255))}


def opt_disp(
): return f"{bnf[option[0]][0]}到{bnf[option[1]][0]}，数字范围{rnr[option[2]][0]}"


def check_opt(opt): return opt_reg.match(opt) != None


def greet():
	print('''\
Suyc v0.1
Copyright (C) 2019 UniGasiX
Licensed under GPL v3.0
欢迎使用Suyc！
您可以使用本程序练习以加快您手动进行整数的2、8、10、16进制间转换的速度
''')


def change_conf():
	global option  # 这里不设置会解析不正常
	print("当前练习设置：" + opt_disp())
	yn = ""
	while True:
		yn = input("是否使用当前设置？[Y/n]: ").lower()
		if yn in {"", "y", "n"}:
			break
		elif yn == "q":
			return False
	if yn == "n":
		print(f'''
请按照 源进制 目标进制 数字范围 的顺序输入新的设置的序号。
可用的设置序号如下：
  进制： {"  ".join(list((k + ": " + v[0]) for k, v in bnf.items()))}
  数字范围： {"  ".join(list((k + ": " + v[0]) for k, v in rnr.items()))}
如：当前设置 {opt_disp()} 需要的输入为 {option}''')
		while True:
			opt = input(">>> ")
			if check_opt(opt):
				option = opt
				break
			else:
				print("** 输入不合规，请重新输入 **")
		print("新的设置：" + opt_disp())
	return True


def run_game() -> bool:
	print("即将开始10道 " + opt_disp())
	input("请按回车键开始...")
	total = timedelta(0)
	for i in range(10):
		r = rnr[option[2]][1]
		num = random.randint(r[0], r[1])
		current = timedelta(0)
		while True:
			in_str = f"  [{i + 1}] {format(num, bnf[option[0]][1])} : "
			start = datetime.now()
			ans = input(in_str)
			end = datetime.now()
			current += end - start
			if ans == "q":
				return True
			elif int(ans, [2, 8, 10, 16][int(option[1]) - 1]) == num:
				print("正确！本题耗时：" + str(current))
				break
			else:
				print("** 错误！请重试 **  | 本题已耗时: " + str(current))
		total += current
	print(f'''-- 本轮练习结束 ----------
    总耗时: {total}
    平均耗时: {total / 10}''')
	choice = ""
	while True:
		choice = input("是否再来一轮？[Y/n]: ").lower()
		if choice in {"", "y", "n"}:
			break
	if choice == "n":
		return False
	else:
		return True


def goodbye():
	print('''-----------------------------------------
再见 ~ ~''')
	input("按回车键结束程序......")


def main():
	if not check_opt(option):
		print("** 代码中的设置字符串不合规！ **")
	greet()
	while True:
		if not change_conf():
			break
		if not run_game():
			break
	goodbye()


main()
