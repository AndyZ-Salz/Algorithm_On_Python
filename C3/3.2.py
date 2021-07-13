# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : 3.2
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""


# History:
# 2021/2/23: Create


def two_sum_1(nums, target):
    res = []
    newnums = nums[:]
    newnums.sort()
    left = 0
    right = len(newnums) - 1

    while left < right:
        if newnums[left] + newnums[right] == target:
            for i in range(0, len(nums)):
                if nums[i] == newnums[left]:
                    res.append(i)
                    break
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == newnums[right]:
                    res.append(i)
                    break
            res.sort()
            break
        elif newnums[left] + newnums[right] < target:
            left = left + 1
        elif newnums[left] + newnums[right] > target:
            right = right - 1

    print(nums)
    print(res)
    return (res[0] + 1, res[1] + 1)


def two_sum_2(nums, target):
    dict = {}
    for i in range(len(nums)):
        m = nums[i]
        if target - m in dict:
            print(dict[target - m] + 1, i + 1)
            return (dict[target - m] + 1, i + 1)
        dict[m] = i


if __name__ == '__main__':
    two_sum_1([3, 7, 4, 10, 5], 11)
    two_sum_2([3, 7, 4, 10, 5], 11)
