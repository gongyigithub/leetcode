#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 10:08:11
# @Author  : gongyi

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''合并两个有序链表，类似于归并排序，直接比较'''
        new = ListNode(None)
        cur = new
        while l1 and l2:
            if l1.val < l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        if l1:
            new.next = l1
        if l2:
            new.next = l2
        return cur.next

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
