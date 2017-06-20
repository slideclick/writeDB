# -*- coding: UTF-8 -*-
#python 3 中文
bytes.fromhex('e6 96 b0 e6 b5 aa e9 a6 96 e9 a1 b5') # 新浪首页 的utf-8编码
chr(ord(bytes.fromhex('e6 96 b0').decode())) #ord显示这个解码后的char的整数值 utf-8 default
hex(ord(bytes.fromhex('e6 96 b0').decode()))