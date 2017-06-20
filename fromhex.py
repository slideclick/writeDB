# -*- coding: UTF-8 -*-
#python 3 中文
bytes.fromhex('e6 96 b0 e6 b5 aa e9 a6 96 e9 a1 b5') # 新浪首页 的utf-8编码
chr(ord(bytes.fromhex('e6 96 b0').decode())) #ord显示这个解码后的char的整数值 utf-8 default
hex(ord(bytes.fromhex('e6 96 b0').decode()))#显示这个utf-8字节串，解码为char后，它的码点
chr(0x65b0) # 它返回一个char

str(b'\xe6\x96\xb0', 'utf-8') #构造出来一个char 
chr(0x65b0).encode('utf-8')
str(b'e\xb0', 'utf-16-be') #它从65b0构造出了一个char.这是大端，如果是小端是 b065 如下
str(b'\xb0e', 'utf-16-le')# 居然utf-16 就是 utf-16-le
