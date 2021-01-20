import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    """
    For first need to read all characters of path one by one using for loop.
    Then check if the character is equals to the U (UP) or D (DOWN)

    Initialize empty variables => level, valley

    Then check if character equals = U (UP)
        increase level by one => level + 1
    If level already was 0 , then anyway increase it by one.
    And if the character doesnt equals to = U (UP)
    then that means that character is D (DOWN) so we need
    to decrease level by one to down => level - 1
    :param steps:
    :param path:
    :return:
    """
    level = valley = 0
    for i in range(len(path)):
        if path[i] == 'U':
            level +=1
            if level == 0:
                valley +=1
        else:
            level -= 1

    print(f" VALLEY = {str(valley)}")
    print(f" LEVELS = {str(level)} ")
    return valley


if __name__ == '__main__':
    countingValleys(8, "UDDDUDUU")
    countingValleys(100, "DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD")
