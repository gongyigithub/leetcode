#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-03 22:23:49
# @Author  : gongyi

# 两数相加  两个单链表表示数字，将两个单链表表示的数字加起来，和作为另外一个单链表输出
# 2->4->3  5->6->4
# 7->->0->8

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

    def __repr__(self):
        return self.val

def addTwoNum(l1,l2):
    head = cur = ListNode(0)
    count = 0
    #注意这里while条件，l1和l2不一定相同长度，所以不能用and
    while l1 or l2:
        #这个转换是为了有些情况，l1和l2长度不一致
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        #将值加起来，这里用sum代替和，不用直接放进节点里
        sum = v1 + v2 + count
        #不管有没有进位，都可以除一下，小于10的数除以10取整就是0
        count = sum // 10
        #利用sum除以10的余数，建立新节点，cur.next指向新节点。也就是head.next
        cur.next = ListNode( sum % 10 )
        # 将cur向前移动，此时cur就是新节点。之后会再次建立新节点并将cur前移
        cur = cur.next
        #还是因为不一定等长，所以要判断还存不存在才能前移
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    # 这里，如果最后有进位，l1和l2已经计算完了，也得把进的那个1加到链表里
    if count > 0:
        cur.next = ListNode(count)
    # 返回head.next，也就是建立的第一个新节点
    return head.next







