def aaa(n) :   
    if n == 1 :
        return 10
    return aaa(n - 1) + 2
print(aaa(5))