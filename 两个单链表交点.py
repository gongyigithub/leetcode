#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-19 10:46:00
# @Author  : gongyi

#查找单链表交叉点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        寻找两个单链表的交叉点，初步思路是循环遍历两个单链表进行比较，相等就判断是否为0，不为0就是相交节点。不相等就继续向前
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1,p2 = headA,headB
        if not (headA and headB):
            return None
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA

        return p2




