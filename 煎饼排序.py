#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-12 11:33:18
# @Author  : gongyi

#通过k煎饼式反转对数组排序，每次反转k，最后输出k的列表
#先找最大值max，下标i
#k=i，执行反转，将最大值换到首部
# k=len(nums)，反转，将最大值换到尾部
#重复这个过程
import pysnooper


class Solution:
    @pysnooper.snoop()
    def pancakeSort(self,nums):
        '''
        对nums中的元素依次执行k反转，使得nums最后有序
        in param nums:数组/列表
        return：k的列表
        '''
        result = []
        #反转
        while nums:
            #先求最大值和索引i
            N = len(nums)
            if N == 1:
                return result
            maxNum = max(nums)
            i = nums.index(maxNum)
            #反转0到i处的列表，最大值到了首位
            nums1 = list(reversed(nums[:i+1]))
            result.append(i+1)
            #反转全部列表，最大值到了尾部
            nums = list(reversed(nums1+nums[i+1:]))
            result.append(N)
            nums.pop()

        #返回k值集合列表
        return result

nums = [3,2,4,1]
res = Solution().pancakeSort(nums)
print(res)


