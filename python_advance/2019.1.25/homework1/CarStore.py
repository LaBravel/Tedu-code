from Car import *
from Customer import *
class CarStore :
    def __init__(self,cars,customers) :
        self.cars = cars
        self.customers = customers
        self.cars000 = []
    
    def __load_cars(self) :#加载所有车辆信息
        self.cars += self.cars000
        self.cars000.clear()

    def __load_customers(self) :#加载所有客户信息
        self.customers = customers

    def print_cars_info(self) :#打印所有车辆信息
        CarStore.__load_cars(self)
        for i in self.cars :
            print(i)
            print('----------------------------------------')

    def find_car(self,car_num) :#查找车辆
        CarStore.__load_cars(self)
        for i in self.cars :
            if car_num in str(i) :
                print('========已经找到========')
                print(i)
        print('查找完毕!')

    def add_car(self,car_id,name,is_lend,price,start_date,end_date) :#添加车辆
        Car0 = Car(car_id,name,is_lend,price,start_date,end_date)
        self.cars.append(Car0)
        print('添加完毕')

    def del_car(self,car_num) :#删除汽车
        for i in self.cars :
            if car_num in str(i) :
                del self.cars[self.cars.index(i)]
        print('删除成功!')

    # def lend(self) :#租车



    # def back(self) :#还车


