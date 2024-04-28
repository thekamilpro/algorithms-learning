def countlist(list):
    if list == []:
        return 0
    
    return 1 + countlist(list[1:])
    
print(countlist([1,2,3,4,5]))