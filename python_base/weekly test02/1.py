for a in range(1,21) :
    for b in range(1,34) :
        for c in range(1,101) :
            if 5 * a + 3 * b + 1 * c == 100  and a + b + 3 * c == 100:
                print({'公鸡':a,'母鸡':b,'小鸡':3 * c})