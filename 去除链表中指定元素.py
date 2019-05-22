#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-22 09:07:15
# @Author  : gongyi

#移除链表中的指定元素
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #先判断当head为空时，直接返回
        if not head:
            return head
        #构建虚拟节点cur，指向head
        cur = ListNode(None)
        cur.next = head
        new = cur
        #从虚拟节点开始遍历
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return new.next

    def removeElements1(self, head, val):
        """
        递归写法，占用空间更多。对每一个节点，如果值等于val，就返回next，否则返回本身
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        head.next = self.removeElements(head.next,val)
        return head.next if head.val==val else head
