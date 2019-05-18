#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-03 16:15:34
# @Author  : gongyi

class listNode():
    def __init__(self,val):
        self.value = val
        self.next = None

    def add(self,val):
        node = listNode(val)
        self.next = node
        self = node

    def size(self):
        current = self.next
        count = 1
        while current != None:
            count += 1
            current = current.next
        return count

def sortList(head):
    '''
    链表排序，nlogn和常数级别空间复杂度.
    归并排序，先快慢指针找到中间结点，再两边归并
    '''
    if head == None or head.next == None:
        #只有一个节点
        return head
    else:
        #有多个节点

        #快慢指针找中间结点
        #快指针每次移动两位，慢指针每次移动一位，当快指针移动到末尾时，慢指针指向中间
        fast,slow = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        head1 = slow.next
        slow.next = None
        l1 = sortList(head)
        l2 = sortList(head1)

        head = new = listNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        if l1 and not l2:
            new.next = l1
        if l2 and not l1:
            new.next = l2
        return head.next

a = listNode(0)
a.add(4)
print(a.value,a.next.value,a.size())
a.add(2)
print(a.value,a.next.value,a.size())
a.add(1)
print(a.value,a.next.value,a.size())
a.add(3)
print(a.value,a.next.value,a.size())

