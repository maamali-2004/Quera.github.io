def samavar(x):
    if x > 100:
        print("Steam")
    elif x < 0:
          print("Ice")
    elif x <= 100 and x >= 0:
        print("Water")
x = int(input())
samavar(x)