class A :
    def __init__(self,name) :
        self.name = name
    
    def __enter__(self) :
        print('__enter__()方法被执行')
        return self

    def __exit__(self,exc_type,exc_val,exc_tb) :
        print('__exit__()方法被执行')

if __name__ == '__main__' :
    with A('GuGu') as a :
        print('with语句执行了')
    print('程序退出')