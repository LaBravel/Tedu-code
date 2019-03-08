from Account import *
class Test(Account) :
    pass

test = Test('1234567890123','LaBrvel','2018年4月1日','借记卡','normal',1000)
test.diposite(500)
test.draw(500)
test.report_loss()
test.diposite(500)
test.relieve_loss()
test.diposite(500)
test.freeze()
test.diposite(500)
test.draw(500)
test.unfreeze()
test.diposite(500)
test.draw(500)
