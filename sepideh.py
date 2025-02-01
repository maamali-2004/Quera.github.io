# def tehrn(n, m):
#     lst = m * [0]
#     i = 0
#     while n > 0:
#         lst[i] += 1
#         i += 1
#         n -= 1
#         if i == m :
#             i = 0
#     return lst[0]
# n, m = map(int, input().split())
# print(tehrn(n, m))
x = int(input())
lst = []
for i in range(x):
    y, z = map(int, input().split())
    lst.append(y)
    lst.append(z)
print(lst)
print()
for i in lst:
    print(i, end=" ")
# for i in lst:
#     print(i) 