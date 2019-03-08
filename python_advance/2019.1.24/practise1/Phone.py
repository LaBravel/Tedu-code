class Phone :
    def __init__(self,name,price,CPU,screen_size) :
        self.name = name
        self.price = price
        self.CPU = CPU
        self.screen_size = screen_size
        self.__caller = ''
        self.__sender = ''
        self.__msg_txt = ''

    def startup(self) :
        print('手机开机')
    
    def shutdown(self) :
        print('手机关机')

    def call(self) :
        self.__caller = input('给谁打电话?')
        print('给%s打电话' % self.__caller)

    def send_msg(self) :
        self.__sender = input('给谁发短信?')
        self.__msg_txt = input('发什么内容')
        print('收信人%s\n%s' % (self.__sender,self.__msg_txt))

    def print_info(self) :
        print('手机名称:%s,手机价格:%d,手机CPU:%s,屏幕尺寸:%d' 
            % (self.name,self.price,self.CPU,self.screen_size))

    def __del__(self) :
        print('__del__方法被调用')