def score(lst):
    result = []
    lst = sorted(lst, reverse=True)
    count = 1
    j = 1
    for i in range(len(lst)):
        if i == 0:
            if lst[i] == lst[i+1]:
                result.append(j)
                count += 1
            else:
                result.append(j)
                count += 1
        else:
            if lst[i] == lst[i-1]:
                result.append(j)
                count += 1
            else:
                j = count
                result.append(j)
                count += 1
    return result
    
number = list(map(int, input().split()))
print(score(number))





