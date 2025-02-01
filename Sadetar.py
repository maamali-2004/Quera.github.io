def sadetar(lst):
    Sum = sum(lst)
    print(f'Sum : {Sum :.6f}')
    ave = Sum / 4
    print(f'Average : {ave :.6f}')
    produc = 1
    for i in lst:
        produc *= i
    print(f'Product : {produc :.6f}')
    maxx = max(lst)
    print(f'MAX : {maxx :.6f}')
    minn = min(lst)
    print(f'MIN : {minn :.6f}')
lst = []
for i in range(4):
    x = int(input())
    lst.append(x)
sadetar(lst)
