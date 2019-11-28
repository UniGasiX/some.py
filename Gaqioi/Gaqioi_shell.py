# 约定了两个占位符： ABRACADABRA1、ABRACADABRA2
# 注意这段代码有特别多的限制，
# 比如：必须是单行程序、只能用单引号、不得有不允许字符……


with open(__file__,'r') as f: exec('ABRACADABRA1'+f.read().replace('\\','\\\\').replace('\'','\\\'')+'ABRACADABRA2')
