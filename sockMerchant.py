#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby


def group(data: list) -> zip:
    """
    This function is used to return grouped identical numbers
     in the one array. It will make randomized array
     more readable for humans.
    :param data:
    :return:
    """
    return [list(v) for k, v in groupby(data)]


def pair(data, num):
    """
    Current function will group elements inside array.
    For this challenge is important to group elements
    by two.

    for example :
        if you got an array like [5,5,3,3,3]
        and then we will try to group it by any position which is not two,
        then we will have one not paired element like below.
         paired by 3 = [[5,5,3], [3,3]]
        but if we group it by two the result will be correct.
            paired by 2 = [[5,5], [3,3]]
        and as we see the last number (3) was removed because
        there is no pair for this one.
    :param data:
    :param num:
    :return:
    """
    return zip(*[iter(data)] * num)


def sockMerchant(n, inp):
    """
    For first we need to sort randomized input array.
    then initialize an empty array socks=[].
    once input array is sorted then we need to group
    all identical elements must be in the one array => [[1, 1, 1, 1], [2], [3, 3, 3, 3, 3]].
    After segregation we should check if the length of grouped array is more than one.
    The group our sub array by every second element => [[1, 1], [1, 1], [3, 3], [3, 3]].
    And at the end just count all the elements of the array and return it as an integer
    :param n:
    :param inp:
    :return:
    """
    inp.sort()
    socks = []
    grouped = group(inp)
    print(grouped)
    for element in grouped:
        if element:
            if len(element) > 1:
                paired_data = pair(element, 2)
                for item in paired_data:
                    if item[0] == item[1]:
                        socks.append([item[0], item[1]])
    flag = len(socks)
    print(socks)
    print(flag)
    return flag


if __name__ == '__main__':
    sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    sockMerchant(15, [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5])
    sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3])
    sockMerchant(20, [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5])
