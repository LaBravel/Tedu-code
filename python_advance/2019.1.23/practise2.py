import random
class AutoMobile :
    #构造方法，主要作用是对属性进行初始化
    def __init__(self,name,color,output_volumn) :
        self.name = name
        self.color = color
        self.output_volumn = output_volumn
        self.__distance = 0.00#行驶里程,私有属性
        self.__fuel_cons = 8.0 
    
    def startup(self) :#启动方法
        print('汽车启动')
    
    def run(self) :#行驶方法
        self.__calc_distance()
        real_fuel_con = self.__fuel_cons / 100 * self.__distance
        print('汽车行驶了%.2f公里,油耗%.2f升' % (self.__distance,real_fuel_con))
    
    def stop(self) :#停止方法
        print('汽车停止')
    
    def __calc_distance(self) :
        a = float(random.uniform(1,400))
        self.__distance += a#改变行驶里程
    
    def get_distance(self) :#获得行驶里程
        return self.__distance

    def info(self) :#打印信息
        print('名称:%s,颜色:%s,排量:%.2f' % 
        (self.name,self.color,self.output_volumn))

if __name__ == '__main__' :
    am = AutoMobile('家用轿车','红色',2.0)
    am.startup()
    am.run()
    am.stop()
    am.info()
    print('行驶里程：%.2f' % am.get_distance())

