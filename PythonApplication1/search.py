def linear_search(li,v):#顺序查找
    for index, val in enumerate(li):
        if v==val:
           return index
    else:
        return None
