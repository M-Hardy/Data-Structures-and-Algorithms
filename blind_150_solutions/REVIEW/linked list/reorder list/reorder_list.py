# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    # O(n) time, O(1) space
    # The trick is to reverse the 2nd half
    # of the linked list - that's how you go 
    # backward in a linked list. 
    def reorderList(self, head):
        
        # get midpoint with slow-fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # separate linked list into 2 halves
        # mid is pointer for second half, 
        # dereference pointer in first half 
        # that points to second half
        mid = slow.next
        slow.next = None
        
        # reverse 2nd half of linked list
        prev = None
        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp
        
        # iterate through original and 2nd reversed
        # linked list, insert reversed list nodes into
        # first list
        while head and prev:
            tmp_head = head.next
            tmp_prev = prev.next            
            
            head.next = prev
            prev.next = tmp_head
            
            head = tmp_head
            prev = tmp_prev
            
    
    def reorderList2(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        l = 0
        r = len(nodes) - 1

        while l < r:
            nodes[r-1].next = None
            tmp = nodes[l].next
            nodes[r].next = tmp
            nodes[l].next = nodes[r]
            l += 1
            r -= 1

        return nodes[0]