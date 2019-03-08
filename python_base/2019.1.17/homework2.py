L = [
    '%s%02s' % (i,j) for i in ['\u2660','\u2663','\u2665','\u2666'] 
    for j in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    ]
L.extend(['JOKER','joker'])
L = set(L)
def fapai(list) :
    import random
    a = set(random.sample(list,17))
    list -= a
    print(a)
while 1 :
    if len(L) <= 3 :
        print('所有牌已经发光')
        print('底牌为',L)
        break
    else :
        c = input('按回车给一个人发牌')
        if c == '' :
            fapai(L)
        else :
            pass
