# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _findMid(self, head):
        '''
        :param head:链表头结点
        :return : 链表中间的那个结点
        '''
        pre = slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        if pre:
            pre.next = None
        
        return slow
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        快慢指针找到中点，作为树的根节点，再遍历链表插入
        '''
        # 快慢指针
        if not head:
            return head
        mid = self._findMid(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
    