with open(__file__, 'r') as f: exec('try:\n    from MyQR import myqr\n    name = input(\u0022Gaqioi\\nCopyright (C) 2019 UniGasiX\\nLicensed under GPL v3.0\\n\u8bf7\u6307\u5b9a\u8f93\u51fa\u56fe\u7247\u7684\u6587\u4ef6\u540d\uff08\u4e0d\u542b\u6269\u5c55\u540d\uff09\uff1a\u0022)\n    myqr.run(\'' + f.read().replace('\\', '\\\\').replace('\'', '\\\'') + '\', save_name=name+\u0022.png\u0022)\nexcept ModuleNotFoundError:\n    print(\u0022\u9519\u8bef\uff01\u8fd9\u6bb5\u7a0b\u5e8f\u9700\u8981MyQR\u5e93\u3002\\n\u53ef\u4ee5\u5c1d\u8bd5\u547d\u4ee4 pip3 install myqr \u5b89\u88c5MyQR\u5e93\u3002\u0022)\n') # Copyright (C) 2019 UniGasiX | Licensed under GPL v3.0 | ATTENTION!!!: The MyQR module is needed. You may try ** pip3 install myqr ** to install.