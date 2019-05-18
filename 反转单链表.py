#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 09:37:02
# @Author  : gongyi

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        迭代法反转单链表。定义两个指针pre、cur分别指向None和头结点head。当cur指向不为None时，就先将cur.next指向pre，即反转。再向前移动两个指针，pre=cur，cur=cur.next。持续遍历
        '''
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList1(self,head):
        '''
        递归法反转单链表。先将头结点指向None，反转以第二个节点为头结点的子链表，赋值给new_head，再将头结点加入这个子链表的尾部。
        '''
        #递归基线条件，链表为空或者只有一个子结点
        if head is None or head.next is None:
            return head
        #第二个结点
        tmp = head.next
        #将头结点指向None
        head.next = None
        #反转第二个结点开头的子链表
        new_head = self.reverseList1(tmp)
        tmp.next = head
        return new_head

