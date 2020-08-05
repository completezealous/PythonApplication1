def select_sort_simple(li):
    for i in range(len(li)-1):#i是第几趟
        min_loc=i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]:
                min_loc=j
        li[i],li[min_loc]=li[min_loc],li[i]

li=[3,4,2,1,4,5,6,5,7]
select_sort_simple(li)
print(li)
