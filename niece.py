def niece(x):
    if x % 2 == 1:
        print("No")
    else:
        if x < 4 :
            print("Yes")
        else:
            if x == 10 :
                print("Yes")
            else:
                print('No')
x = int(input())
niece(x)