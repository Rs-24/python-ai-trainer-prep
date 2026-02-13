# Time to write all of below including tests, explanation and time and aux 
# space: 27 mins

# Problem: https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        while list1:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next
        return dummy.next

def to_list(head: Optional[ListNode]):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.mergeTwoLists(None, None) == None
    
    l1 = ListNode(1)
    assert sol.mergeTwoLists(l1, None) == l1

    l2 = ListNode(1, ListNode(2))
    assert sol.mergeTwoLists(None, l2) == l2

    l1 = ListNode(-1, ListNode(0, ListNode(1)))
    l2 = ListNode(0, ListNode(1, ListNode(3)))
    assert to_list(sol.mergeTwoLists(l1, l2)) == [-1, 0, 0, 1, 1, 3]

# Explanation: the code creates a new linked list, and iterates over both
# input linked lists. It compares the nodes of each linked list, and joins the
# node with the smaller value to the new linked list. Once the loop ends, the
# code iterates through any remaining nodes in list1 or list2 and joins them
# to the new linked list
# Time: O(n + m), n = number of nodes in list1, m = number of nodes in list2
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(n + m)

# Learning lessons (done after completing all of above in 27 mins):
#   - No major learning lessons


