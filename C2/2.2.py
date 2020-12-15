# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : 2.2
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""


# History:
# 2020/8/18: Create


def binary_search():
    numbers = [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]
    head, tail = 0, len(numbers)  # length = max index+1
    search = int(input("Enter a number to search:"))
    while tail - head >1: #tail - head =1 means only tail is available num
        mid = (head+tail)//2
        if search < numbers[mid]:
            tail = mid
        elif search > numbers[mid]:
            head = mid+1
        else:           # search == numbers[mid]
            ans = mid
            break
    else:
        if search == numbers[head]:
            ans =head
        else:
            ans = -1
    print(ans)


if __name__ == '__main__':
    binary_search()
