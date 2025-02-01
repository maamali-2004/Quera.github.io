def bagher():
    # total = 0
    lamp = 0 
    wait = 0
    # nowmin = 0
    n, l = map(int, input().split())
    lst = []
    for i in range(n):
        di, ri, gi = map(int, input().split())
        lst.append(di)
        lst.append(ri)
        lst.append(gi)
    
    res = l
    for i in range(0, len(lst), 3):
        
        if lst[i]+lamp < lst[i+1]:
            lamp = lst[i+1] - lst[i]
            res += lamp
        else:
            time = 0
            while time <= lst[i] + lamp:
                time += lst[i+1]
                if time <= lst[i] + lamp:
                    time += lst[i+2]
                    if time >= lst[i] + lamp:
                        break #green
                else:
                    wait = time - (lst[i] + lamp)
                    lamp += wait
                    res += lamp
                    break
    return res
print(bagher())
        
        
        
        
        
        
        
        
        
    