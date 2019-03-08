def numb_chinese(x) : 
    j = 0
    for i in x :
        if 0x4E00 <= ord(i) <= 0x9FA5 :
            j += 1
    return j
print("这段文字中有",numb_chinese(input("请输入一段字符")),"个中文字符")