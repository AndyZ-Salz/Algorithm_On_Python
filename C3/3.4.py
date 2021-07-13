# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : 3.4
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""


# History:
# 2021/2/24: Create


def get_hint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :return: str
    """
    secret_dict = {}
    guess_dict = {}

    A = 0
    B = 0

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            A += 1
        else:
            if secret[i] in secret_dict:
                secret_dict[secret[i]] = secret_dict[secret[i]] + 1
            else:
                secret_dict[secret[i]] = 1
            if guess[i] in guess_dict:
                guess_dict[guess[i]] = guess_dict[guess[i]] + 1
            else:
                guess_dict[guess[i]] = 1

    for digit in secret_dict:
        if digit in guess_dict:
            B += min(secret_dict[digit], guess_dict[digit])

    return str(A) + "A" + str(B) + "B"


if __name__ == '__main__':
    print(get_hint("1234", "1321"))
