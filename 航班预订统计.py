#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-01 22:07:13
# @Author  : gongyi

'''
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.
----bookings[i]表示从第i个到第j个航班，每个航班都订了k个座位
Return an array answer of length n, representing the number of seats booked on each flight in order of their label.
----返回一个数组，长度为n，即航班数，元素是按航班顺序排列的每个航班被预定的座位数
'''

def corpFlightBookings(bookings,n:int):

    # 创建result空列表，存储最终结果
    result = [0]*n
    print(result)
    for i in bookings:
        print('预订信息:',i)
        for j in range(i[0],i[1]+1):
            print('当前航班：',j,'数量：',i[2])
            result[j-1] += i[2]

    print(result)
    return result


def corpFlightBookings1(bookings,n:int):

    # 前缀和法。
    res = [0] * n
    for i,j,k in bookings:
        res[i-1] += k
        if j < n:
            res[j] -= k
        print(res)
    for i in range(1,n):
        res[i] += res[i-1]
    print(res)
    return res

def so(bookings,n):
    # 扫描线解法
    ans = [0] * n
        d = dict()
        for start, end, val in bookings:
            d[start - 1] = d.get(start - 1, 0) + val
            d[end] = d.get(end, 0) - val
        s = 0
        for i in range(n):
            if i in d:
                s += d[i]
            ans[i] = s
        return ans

bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
corpFlightBookings1(bookings,n)
