# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : 2.3
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""


# History:
# 2020/12/10: Create


def linked_list_1():
    ListValue = [1, 5, 6, 2, 4, 3]
    ListPointer = [3, 2, -1, 5, 1, 4]
    head = 0
    print(ListValue[head])
    next = ListPointer[head]
    while next != -1:
        print(ListValue[next])
        next = ListPointer[next]
    print()


def linked_list_2():
    value = 0
    pointer = 1
    LinkedList = [[1, 3], [5, 2], [6, -1], [2, 5], [4, 1], [3, 4]]
    head = 0
    print(LinkedList[head][value])
    next = LinkedList[head][pointer]

    while next != -1:
        print(LinkedList[next][value])
        next = LinkedList[next][pointer]
    print()


def du_link_list_1():
    print("method1")
    ListValue = [1, 5, 6, 2, 7, 3]
    ListRight = [3, 2, 4, 5, -1, 1]
    ListLeft = [-1, 5, 1, 0, 2, 3]

    head = ListLeft.index(-1)
    print(ListValue[head])
    Next = ListRight[head]

    while Next > -1:
        print(ListValue[Next])
        Next = ListRight[Next]
    print()

    print("method2")
    right = 1
    left = 2
    value = 0
    LinkedList = [[1, 3, -1], [5, 2, 5], [6, 4, 1], [2, 5, 0], [7, -1, 2], [3, 1, 3]]
    head = 0
    print(LinkedList[head][value])
    Next = LinkedList[head][right]

    while Next > -1:
        print(LinkedList[Next][value])
        Next = LinkedList[Next][right]
    print()


def du_link_list_2():
    print("Forward")
    ListValue = [1, 5, 6, 2, 7, 3]
    ListRight = [3, 2, 4, 5, -1, 1]
    ListLeft = [-1, 5, 1, 0, 2, 3]

    head = ListLeft.index(-1)
    print(ListValue[head])
    Next = ListRight[head]

    while Next > -1:
        print(ListValue[Next])
        Next = ListRight[Next]

    print("Reverse")
    head = ListRight.index(-1)
    print(ListValue[head])
    Next = ListLeft[head]

    while Next > -1:
        print(ListValue[Next])
        Next = ListLeft[Next]
    print()


def linkedList_addElement():
    def Output(ListValue, ListRight, head):
        print(ListValue[head])
        next = ListRight[head]
        while next != -1:
            print(ListValue[next])
            next = ListRight[next]

    ListValue = [1, 5, 6, 2, 7, 3]
    ListRight = [3, 2, 4, 5, -1, 1]
    head = 0
    prepos = 5

    print("pre-add")
    Output(ListValue, ListRight, head)  # pre-add
    print()

    ListValue.append(4)
    ListRight.append(ListRight[prepos])
    ListRight[prepos] = len(ListValue) - 1

    print("added")
    Output(ListValue, ListRight, head)  # added
    print()


def duLinkedList_addElement():
    def Output(ListValue, ListRight, head):
        print(ListValue[head])
        next = ListRight[head]
        while next != -1:
            print(ListValue[next])
            next = ListRight[next]

    ListValue = [1, 5, 6, 2, 7, 3]
    ListRight = [3, 2, 4, 5, -1, 1]
    ListLeft = [-1, 5, 1, 0, 2, 3]
    head = 0
    prepos = 5

    print("pre-add")
    Output(ListValue, ListRight, head)  # pre-add
    print()

    ListValue.append(4)
    ListRight.append(ListRight[prepos])
    ListLeft.append(prepos)
    ListLeft[ListRight[prepos]] = len(ListValue) - 1
    ListRight[prepos] = len(ListValue) - 1

    print("added")
    Output(ListValue, ListRight, head)  # added
    print()


def linkedList_deleteElement():
    def Output(ListValue, ListRight, head):
        print(ListValue[head])
        next = ListRight[head]
        while next != -1:
            print(ListValue[next])
            next = ListRight[next]

    ListValue = [1, 5, 6, 2, 7, 3]
    ListRight = [3, 2, 4, 5, -1, 1]
    head = 0
    prepos = 5

    print("pre-delete")
    Output(ListValue, ListRight, head)  # pre-delete
    print()

    ListRight[prepos] = ListRight[ListRight[prepos]]

    print("deleted")
    Output(ListValue, ListRight, head)  # deleted
    print()


def duLinkedList_deleteElement():
    def Output(ListValue, ListRight, head):
        print(ListValue[head])
        next = ListRight[head]
        while next != -1:
            print(ListValue[next])
            next = ListRight[next]

    ListValue = [1, 5, 6, 2, 7, 3]
    ListRight = [3, 2, 4, 5, -1, 1]
    ListLeft = [-1, 5, 1, 0, 2, 3]
    head = 0
    prepos = 5

    print("pre-delete")
    Output(ListValue, ListRight, head)  # pre-delete
    print()

    ListRight[prepos] = ListRight[ListRight[prepos]]
    ListLeft[ListRight[ListRight[prepos]]] = prepos

    print("deleted")
    Output(ListValue, ListRight, head)  # deleted
    print()


if __name__ == '__main__':
    linked_list_1()
    linked_list_2()
    du_link_list_1()
    du_link_list_2()
    linkedList_addElement()
    duLinkedList_addElement()
    linkedList_deleteElement()
    duLinkedList_deleteElement()
