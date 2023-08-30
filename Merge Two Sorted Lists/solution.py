from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def helper(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = list1

        while node.next != None and list2 != None:
            if node.next.val  < list2.val:
                node = node.next
            else:
                tmp = node.next
                node.next = list2
                node = tmp

                while list2.next != None and list2.next.val <= node.val:
                    list2 = list2.next

                tmp = list2.next
                list2.next = node
                list2 = tmp

        if list2 != None :
            node.next = list2

        return list1
    
    def mergeTwoListsContstantInSpaceSolution(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2

        return self.helper( list1 if list1.val < list2.val else list2, list2 if list1.val < list2.val else list1)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2