from CarStore import *
class Test(CarStore) :
    pass

test = Test([Car1,Car2,Car3],[Customer1,Customer2,Customer3])
test.print_cars_info()
test.find_car('001')
test.add_car('004','马自达','未出租',500,'','')
test.print_cars_info()
test.del_car('004')
test.print_cars_info()