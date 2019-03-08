x = float(input("请输入费用金额"))
if 0 < x <= 3 :
    a = round(13.00,2)
    x = '%.2f' % a
    print("费用金额是：",x,"元")
elif 3 < x <= 15 :
    a = round(13.00 + (x - 3.00) * 2.30,2)
    x = '%.2f' % a
    print("费用金额是：",x,"元")
elif 15 < x :
    a = round(27.60 + (x - 15.00) * 3.45,2)
    x = '%.2f' % a
    print("费用金额是：",x,"元")
else :
    print("输入金额无效！")