#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-03 16:23:52
# @Author  : gongyi

# 两两反转单链表
# 1->2->3->4    2->1->4->3

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def swapPair(head):
    #递归写法。以1,2,3,4为例
    if not head or not head.next:
        return head
    next = head.next
    #例如1，2.反转1和2，那么1后边跟的就是剩下的节点，也就是1.next = 剩下所有节点反转
    #再让2.next = 1即可。
    head.next = swapPair(next.next)
    next.next = head
    return next


def swapPair1(head):
    #非递归写法
    pre = ListNode(0)
    pre.next = head
    tmp = pre
    while tmp.next and tmp.next.next:
        #当有head和head.next时
        start = tmp.next  #就是head
        end = tmp.next.next   #就是head.next
        # head变成了2
        tmp.next = end
        # 1的后继节点由2变成3
        start.next = end.next
        # 2的后继节点由3变成1
        end.next = start
        # 将tmp指向1.本来是指向None的，这样tmp.next = 3
        tmp = start
    return pre.next
