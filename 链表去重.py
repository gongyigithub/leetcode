#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-18 14:05:22
# @Author  : gongyi

# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        遍历比较，删除重复元素
        '''
        if not (head and head.next):
            #如果head为空或者head只有一个节点，直接返回其本身
            return head
        first = head
        sec = head.next
        while sec.next:
            if first.val == sec.val:
                #两者值相等，删除first指向的结点
                first.next = sec.next
                #将sec向前移动一位
                sec = sec.next
            else:
                #两者不等，都向前移动一位
                first,sec = sec,sec.next
        #最后sec指向最后一位节点，first指向倒数第二位，如果这俩相等，删除最后一个节点
        if first.val == sec.val:
            first.next = None
        return head
