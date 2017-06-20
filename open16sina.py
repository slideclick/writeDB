with open(r'16sina.htm','r',encoding='utf-16') as csvFile:# little Endian
    for ln in csvFile:
        print(ln)