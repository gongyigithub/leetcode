#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-03 15:59:58
# @Author  : gongyi

# 判断两个字符串J和S里，J中有的字符在S里的个数。
'''
J = "aA", S = "aAAbbbb"
3
'''

def JewelsStones(J,S):
    #时间复杂度O(M*N)
    count = 0
    for i in S:
        for j in J:
            if j == i:
                count += 1
    return count

def JewelsStones(J,S):
    #
    count = 0
    dic = {}
    for i in J:
        dic[i] = 0
    for j in S:

