# coding=utf-8
"""
You are building a diving board by placing a bunch of planks of wood end-to-end. There are two types of planks, one of length shorter and one of length longer. You must use exactly K planks of wood. Write a method to generate all possible lengths for the diving board.
return all lengths in non-decreasing order.
用两种木板首尾相连拼接成跳水板，两种木板一种短一种长，两种木板一共最多可以使用k块。给出两种木板的长度和最多使用木板的个数，要求返回所有可能拼接出的跳水板长度
"""


class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if not k:
            return []
        if shorter == longer:
            return [shorter*k]
        return [shorter*i + longer*(k-i) for i in range(k+1)]


test = Solution()
result = test.divingBoard(2, 1118596, 979)
print(result)
