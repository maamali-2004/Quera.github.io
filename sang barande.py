def sang(x):
    if x == 3 :
         print("NO")
    else:
        if x == 1 :
            print("YES")
        elif x % 2 == 0 :
            sang(x//2)
        elif x % 2 == 1:
            sang((3 * x) + 3)
x = int(input())
sang(x)