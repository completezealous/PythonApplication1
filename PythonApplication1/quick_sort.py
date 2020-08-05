import random
from cal_time import *
def partition(li,left,right):
    tmp=li[left]
    while left<right:
        while left<right and li[right]>=tmp:#从右面找比tmp小的数
            right-=1
        li[left]=li[right]#把右边的值写到左边空位上
        while left<right and li[left]<=tmp:
            left+=1
        li[right]=li[left]
    li[left]=tmp#tmp归位,此时left已成为中间值下标
    return left


@cal_time
def quick_sort(li,left,right):
    if left<right:#至少两个元素
        mid=partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

li=list(range(100))
random.shuffle(li)
quick_sort(li,0,len(li)-1)
print(li)
