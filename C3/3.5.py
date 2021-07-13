# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : 3.5
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2021/7/13: Create
import collections
from typing import List


def replace_words(dict: List[str], sentence: str):
    """
    :param dict: root
    :param sentence: str
    :return: str
    """
    d = collections.defaultdict(set)
    s = collections.defaultdict(int)
    sentence = sentence.split()

    for w in dict:
        print(w[0])
        d[w[0]].add(w)
        s[w[0]] = max(s[w[0]], len(w))
    for i,w in enumerate(sentence):
        print(i,w)
        for j in range(s[w[0]]):
            if w[:j+1] in d[w[0]]:
                sentence[i] = w[:j+1]
                break
    return ' '.join(sentence)


if __name__ == '__main__':
    d = ["cat", "bat", "rat"]
    print(replace_words(d, "the cattle was rattled by the battery"))
