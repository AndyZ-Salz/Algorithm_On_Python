# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : 2.1
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 合并有序数组
---------------------------------------
"""


# History:
# 2020/8/18: Create

def merge():
    arr1 = [1, 3, 4, 6, 10]
    arr2 = [2, 5, 8, 11]
    ind = 0
    ans = arr1.copy()
    for i in range(0, len(arr2)):
        while ind < len(arr1):
            if arr2[i] <= arr1[ind]:
                ans.insert(ind + i, arr2[i])
                break
            else:
                ind += 1
    else:
        ans += arr2[i:]
    print(ans)


if __name__ == '__main__':
    merge()
