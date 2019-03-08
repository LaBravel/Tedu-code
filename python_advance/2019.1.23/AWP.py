class AWP :
    def __init__(self) :#构造方法
        self.name = 'AWP'#名称        
        self.max_bullets = 10#弹夹容量
        self.bullets_left = 0#剩余子弹
        self.destructRatio = 1.0#杀伤系数
    
    def reload(self) :#装弹
        #填弹后剩余子弹等于弹夹容量
        self.bullets_left = self.max_bullets
    
    def fire(self) :#开火
        if self.bullets_left <= 0 :#没子弹
            print('请填弹')
            return
        self.bullets_left -= 1 #打出1发子弹
        #计算杀伤力
        damage = int(self.destructRatio * 100)
        #模拟声音
        print('砰！,杀伤力%d,剩余子弹%d' % (damage,self.bullets_left))