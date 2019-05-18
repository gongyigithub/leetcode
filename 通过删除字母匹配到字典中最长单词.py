#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-14 12:36:25
# @Author  : gongyi

# 给定一个字符串和一个字符串列表，找到列表里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且列表序索引最小的字符串。如果答案不存在，则返回空字符串。

def findLongestWord(s,d):
    '''
    in param s:字符串
    in param d:字符串列表
    '''
    N = len(s)
    flag = False
    current = ''
    for sd in d:
        i,j = 0,0
        while i < N and j < len(sd):
            if s[i] == sd[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j != len(sd):
            #遍历完成，说明每个j里边每个字母都和s中匹配
            continue
        if len(current) < len(sd):
            current = sd
        elif len(current) == len(sd):
            if sd < current:
                current = sd
        else:
            pass

    return current


s = "bab"
d = ["ale","apple","monkey","plea"]
d1 = ["ba","ab","a","b"]
res = findLongestWord(s,d1)
print(res)
