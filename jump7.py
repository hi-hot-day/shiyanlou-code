for a in range(1,101): # a大于等于1，小于101
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7: # 如果 a 可以被7整除，除以10取余为7，除以10取整为7，则跳过，否则打印a
        continue
    else:
        print(a)
