class AK47 :
    def __init__(self) :
        self.name = 'AK47'#名称        
        self.max_bullets = 30#弹夹容量
        self.bullets_left = 0#剩余子弹
        self.destructRatio = 0.4#杀伤系数

    def reload(self) :#装弹
        #填弹后剩余子弹等于弹夹容量
        self.bullets_left = self.max_bullets
    
    def fire(self) :#开火
        if self.bullets_left <= 0 :#没子弹
            print('请填弹')
            return
        if self.bullets_left >= 3 :
            self.bullets_left -= 3 #打出３发子弹
        else :#子弹大于０小于３发
            self.bullets_left = 0#全部打出去
        #计算杀伤力
        damage = int(self.destructRatio * 100)
        #模拟声音
        print('突突突,杀伤力%d,剩余子弹%d' % (damage,self.bullets_left))