'''
Given a string, count 3 most used character in it, print word followed by their num of occurance, if they have same number of occurance then sort them alphabetically and print.

Hackerrank link: https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    occurance = {}
    for char in s:
        if char in occurance:
            occurance[char] += 1
        else:
            occurance[char] = 1
    sorted_occurance = sorted(occurance.items(), key = lambda x: (-x[1], x[0]))[:3]
    
    for group in sorted_occurance:
        print(group[0], group[1])
