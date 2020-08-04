from cal_time import *
@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:    # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: # 带查找的值在mid左侧
            right = mid - 1
        else: # li[mid] < val 带查找的值在mid右侧
            left = mid + 1
    else:
        return None

li = list(range(100000000))
print(binary_search(li, 3890000))
