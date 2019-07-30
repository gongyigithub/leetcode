#coding='utf-8'
'''
 * @authors gongyi (you@example.org)
 * @date    2019-07-24 09:08:55
 * @version $Id$
 '''

class Node():

    def __init__(self,val=None,next=None):
        '''
        初始化节点
        '''
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        count = 0
        cur = self.head
        while cur:
            if count == index:
                return cur.val
            cur = cur.next
            count += 1
        return -1


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        print(self.head.val)
        print('增加头',self.head.val,self.head.next,self.size())

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        cur = self.head
        if not self.head:
            self.addAtHead(val)
        #遍历链表，直到最后一个节点
        while cur.next:
            cur = cur.next
        cur.next = new_node
        print('增加尾',cur.next.val,self.size())



    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        count = 0
        cur = self.head
        #注意临界值
        if index <= 0:
            self.addAtHead(val)
        while cur and count < index - 1:
            #有节点且节点位置不大于index
            cur = cur.next
            count += 1
        if count == index - 1:
            #此时cur是index-1处的节点
            new_node.next = cur.next
            cur.next = new_node



    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        count = 0
        cur = self.head
        #注意临界值
        if index < -1:
            return None
        if index == 0:
            self.head = self.head.next
        while cur and count < index - 1:
            cur = cur.next
            count += 1
        if cur.next:
            cur.next = cur.next.next

    def __repr__(self):
        if not self.head:
            return 'chain is empty'
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.val) + ','
            node = node.next
        return nlist

    def size(self):
        '''
        获得当前链表长度
        '''
        print('计算长度',self.head)
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
        return count

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(1)
obj.addAtHead(1)
print('头结点增加12',obj)
obj.addAtTail(3)
print('尾巴加个13',obj)
obj.addAtIndex(1,2)
print('1这个位置加个11',obj)
print(obj.get(1))
obj.deleteAtIndex(1)
print('删除索引1这儿的值',obj,obj.get(1))
