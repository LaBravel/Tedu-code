import random
AGF,JYF,HXF,YSF,FQF = 0,0,0,0,0
for i in range(100000) :
    a = random.uniform(0,100)
    if 0 <= a < 30 :
        AGF += 1
    elif 30 <= a < 40 :
        JYF += 1 
    elif 40 <= a < 70 :
        HXF += 1 
    elif 70 <= a <= 90 :
        YSF += 1 
    elif 90 <= a < 100 :
        FQF += 1
print('爱国福%.3f%%\n敬业福%.3f%%\n和谐福%.3f%%\n友善福%.3f%%\n富强福%.3f%%' % \
    (float(AGF / 1000),float(JYF / 1000),float(HXF / 1000),float(YSF / 1000),float(FQF / 1000)))