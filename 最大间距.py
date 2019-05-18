#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-08 21:22:10
# @Author  : gongyi

# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

# 如果数组元素个数小于 2，则返回 0。

class Solution:
    def maximumGap(self,nums):
        '''
        限定线性复杂度，可以考虑归并、快排、堆排序。这里归并
        '''
        #这是最大间距值
        maxNum = 0
        N = len(nums)
        if N < 2:
            maxNum = 0
        else:
            mid = N//2
            left = nums[:mid]
            right = nums[mid:]
            self.maximumGap(left)
            self.maximumGap(right)

            #i是left的下标，j是right的下标。k是nums的下标
            i,j,k = 0,0,0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
                #每次循环，都更新maxNum
                if k > 2:
                    maxNum = max(maxNum,(nums[k-1] - nums[k-2]))
            while i < len(left):
                nums[k] = left[i]
                maxNum = max(maxNum,nums[k] - nums[k-1])
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                maxNum = max(maxNum,nums[k] - nums[k-1])
                j += 1
                k += 1

        return maxNum

s = Solution()
nums = [1,10000]
res = s.maximumGap(nums)
print(res)
