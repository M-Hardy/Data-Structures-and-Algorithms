# # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # initialize slow at dummy so that 
        # it is 1 behind node to delete.
        # create dummy so you have pointer to
        # whole list (head) as you traverse with slow.
        # use dummy instead of head in case
        # head itself is removed.
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while n and fast:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next