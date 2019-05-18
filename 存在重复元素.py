#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-09 14:34:58
# @Author  : gongyi

# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

class Solution:
    def conatinNearBy(self,nums,k,t):
        #只要有任意i和j满足条件即可
        N = len(nums)
        result = False
        for i in range(N):
            if i+k+1 > N:
                for j in range(i+1,N):
                    if abs(nums[i] - nums[j]) <= t:
                        print(i,j,nums[i],nums[j])
                        result = True
            else:
                for j in range(i+1,i+k+1):
                    if abs(nums[i] - nums[j]) <= t:
                        print(i,j,nums[i],nums[j])
                        result = True
        return result

nums = [1,5,9,1,5,9]
k = 2
t = 3
res = Solution().conatinNearBy(nums,k,t)
print(res)
