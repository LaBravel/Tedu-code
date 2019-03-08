manager = {'曹操','刘备','孙权'}
tech = {'曹操','孙权','张飞','关羽'}
print('即是经理也是技术员的',manager & tech)
print('是经理但不是技术员的',manager - tech)
print('是技术人员，但不是经理的人有',tech - manager)
print('张飞是经理吗','张飞' in manager)
print('身兼一职的有',manager ^ tech)
print('经理和技术人员共有几个人',manager | tech)