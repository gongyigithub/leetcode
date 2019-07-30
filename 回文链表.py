#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-24 19:43:02
# @Author  : gongyi

#判断给出的单链表是否是回文。要求O(n)time和O(1)space
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        初步想法是快慢指针找到中点，时间复杂度n，空间复杂度1
        再从head和slow遍历比较val是否相等，第二次遍历也是n和1
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        #通过快慢指针找到中点，将原链表分成两部分
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head1 = slow.next
        slow.next = None
        pre = self.reverse(head1)

        #反转完成，此时head1位原链表后半部分的逆序链表，再比较值大小
        if head.val == pre.val:
            head,pre = head.next,pre.next
        else:
            return False
        return True

        def reverse(head):
            if not head:
                return None
            pre = ListNode(None)
        #反转后半部分链表
            while head:
                tmp = head.next
                head.next = pre
                pre = head
                head = tmp
            return pre




def gg(head):
    if head is None or head.next is None:
        return True
    if head.next.next is None:
        return head.val == head.next.val
    fast = slow = q = head
    while fast.next and fast.next.next:#这里快指针的判读条件跟判断环形有一点不同
        fast = fast.next.next
        slow = slow.next

    def reverse_list(head):
        if head is None:
            return head
        cur = head
        pre = None
        nxt = cur.next
        while nxt:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next
        cur.next = pre
        return cur

    p = reverse_list(slow.next)
    while p.next:
        if p.val != q.val:
            return False
        p = p.next
        q = q.next
    return p.val == q.val
