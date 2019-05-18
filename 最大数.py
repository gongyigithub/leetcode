#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-09 14:16:49
# @Author  : gongyi

# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
# 输入: [3,30,34,5,9]
# 输出: 9534330
class Solution:
    def largestNumber(self,nums):
        #看评论，是判断nums中的元素a和b，a+b和b+a的大小关系。直接遍历，计算每一个a+b和b+a的大小关系
        if sum(nums) == 0:
            return 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i],nums[j] = nums[j],nums[i]
        return ''.join(map(str,nums))

nums = [3,30,34,5,9]
res = Solution().largestNumber(nums)
print(res)
