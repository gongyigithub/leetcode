#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-22 14:15:29
# @Author  : gongyi

#判断链表是否有环
# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        快慢指针遍历，如果有环，一定会相遇
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if head == head.next:
            return True
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def hasCycle1(self,head):
        '''
        字典法，将遍历过的节点指针存入字典中，每次检查这个指针是否在字典中存在，存在就说明有环
        '''
        if not head:
            return False
        if head == head.next:
            return True
        dic = {}
        while head:
            if head in dic:
                return True
            else:
                dic[head] = 1
            head = head.next
        return False

