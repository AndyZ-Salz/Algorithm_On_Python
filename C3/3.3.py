# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : 3.3
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""


# History:
# 2021/2/24: Create


def word_pattern(wordPattern, input):
    word = input.split(" ")
    if len(word) != len(wordPattern):
        return False

    hash = {}
    used = {}

    for i in range(len(wordPattern)):
        if wordPattern[i] in hash:
            if hash[wordPattern[i]] != word[i]:
                return False
        else:
            if word[i] in used:
                return False
        hash[wordPattern[i]] = word[i]
        used[word[i]] = True

    return True


if __name__ == '__main__':
    print(word_pattern("1221", "apple banana banana apple"))
    print(word_pattern("1231", "apple banana banana apple"))
    print(word_pattern("121", "apple banana banana apple"))
