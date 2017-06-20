import sys
with open(sys.argv[1],'rt',encoding='gbk') as f:
    with open(sys.argv[2],'a+',encoding='utf-8') as outF:
        for ln in f:
            print(ln)
            outF.write(ln)
        