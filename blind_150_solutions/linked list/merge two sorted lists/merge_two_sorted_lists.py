# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    #iterative
    def mergeTwoLists2(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 if list1 else list2
        
        return dummy.next
  
    
    #recursive
    def mergeTwoLists2(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not list2:
            return list1
        elif not list1:
            return list2
        else:
            small, big = (list1, list2) if list1.val < list2.val else (list2, list1)
            small.next = self.mergeTwoLists(small.next, big)
            return small      