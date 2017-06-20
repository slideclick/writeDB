with open(r'16sina.htm','r',encoding='utf-16-le') as csvFile:# little Endian
    with open(r'utf8sina.htm','a+',encoding='utf-8') as outF:
        for ln in csvFile:
            print(ln)
            outF.write(ln)