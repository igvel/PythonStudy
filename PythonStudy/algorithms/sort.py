# -*- coding: UTF-8 -*-
from random import randrange

__author__ = 'ielkin'


def insert_sort(lst):
    """
     Insertion sort implementation
    """
    length = len(lst)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
            else:
                break
        print lst


def merge_sort(lst):
    """
     Merge sort implementation in-place
    """
    # guard condition
    if len(lst) < 2:
        return lst

    def merge(lst, start, half, end):
        temp = []
        i = start
        j = half + 1
        while i <= half and j <= end:
            if lst[i] < lst[j]:
                temp.append(lst[i])
                i += 1
            else:
                temp.append(lst[j])
                j += 1

        while j <= end:
            temp.append(lst[j])
            j += 1

        while i <= half:
            temp.append(lst[i])
            i += 1

        for k in range(len(temp)):
            lst[start + k] = temp[k]

    def rec_sort(l_in, start, end):
        if start == end:
            return
        half = (start + end) // 2
        rec_sort(l_in, start, half)
        rec_sort(l_in, half + 1, end)
        merge(l_in, start, half, end)

    rec_sort(lst, 0, len(lst) - 1)


def quick_sort(lst):
    """
     Quick sort
    """

    def rec_sort(lst, start, end):
        if start == end:
            return
        p = lst[(start + end) / 2]
        i = start
        j = end

        while i <= j:
            while lst[i] < p:
                i += 1
            while lst[j] > p:
                j -= 1
            if i <= j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
        print(lst)
        if j > start:
            rec_sort(lst, start, j)
        if i < end:
            rec_sort(lst, i, end)

    rec_sort(lst, 0, len(lst) - 1)


lst = [9, 2, 7, 6, 1, 4, 3, 8, 5]
#lst = [randrange(100) for i in range(100)]
#lst.reverse()
print(lst)
quick_sort(lst)
print lst
