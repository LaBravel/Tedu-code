def privileged_check(fn) :
    def fx(n,x) :
        print('正在检查权限')
        fn(n,x)
    return fx

def send_message(fn) :
    def fy(n,x) :
        fn(n,x)
        print('正在发送短信给',n)
    return fy


@privileged_check
def savemoney(name,x) :
    print(name,'存钱',x,'元')

@send_message
@privileged_check
def withdraw(name,x) :
    print(name,'取钱',x,'元')

savemoney('小王',200)
savemoney('小赵',400)
withdraw('小李',500)