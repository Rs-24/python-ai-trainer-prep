# Time to write all of below including tests, explanation and time and aux 
# space: 25 mins

# Problem: https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = None
        
        if list1.val < list2.val:
            head = list1
        else:
            head = list2

        node1 = list1.next
        node2 = list2.next

        while node1 and node2:
            if node1.val < node2.val:
                head.next = node1
                node1 = node1.next
            else:
                head.next = node2
                node2 = node2.next
        
        if not node1:
            while node2:
                head.next = node2
                node2 = node2.next        
        if not node2:
            while node1:
                head.next = node1
                node1 = node1.next        

        return head

if __name__ == "__main__":
    sol = Solution()
    assert sol.mergeTwoLists(None, None) == None
    l1 = ListNode(1)
    assert sol.mergeTwoLists(l1, None) == l1
    l2 = ListNode(0)
    assert sol.mergeTwoLists(None, l2) == l2
    l1 = ListNode(-1, ListNode(0))
    l2 = ListNode(2, ListNode(3))
    l3 = ListNode(-1, ListNode(0, ListNode(2, ListNode(3))))
    assert sol.mergeTwoLists(l1, l2) == l3

# Explanation: Both lists are iterated over and spliced onto head
# Time: O(n + m), n, m = number of nodes in each list
# Aux space: O(n + m)

# Learning lessons (done after completing all of above in 25 mins):
#   - Every time after I assign head.next, I should also have added the
#     line 'head = head.next' as currently I am just rewriting the same
#     head.next each time
#   - After assigning head, I also assign node1 and node2, however I end up
#     skipping the first node of list1 or list2
#   - My rewrite is below:
#
# def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     # Time: O(n + m)
#     # Aux space: O(1)
#     dummy = ListNode(0)
#     tail = dummy
#     while list1 and list2:
#         if list1.val <= list2.val:
#             tail.next = list1
#             list1 = list1.next
#         else:
#             tail.next = list2
#             list2 = list2.next
#         tail = tail.next
#     if list1:
#         tail.next = list1
#     else:
#         tail.next = list2
#     return dummy.next
#
#   - Additionally, my tests wouldn't work as is, I would instead need to
#     convert to lists. I could have also added an interweaving case. My
#     rewrite for my tests are below:
#
# from typing import List
# def to_list(head: Optional[ListNode]) -> List[int]:
#     if not head:
#         return []
#     out = []
#     node = head
#     while node:
#         out.append(node.val)
#         node = node.next
#     return out
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert to_list(sol.mergeTwoLists(None, None)) == []
#     assert to_list(sol.mergeTwoLists(ListNode(1), None)) == [1]
#     assert to_list(sol.mergeTwoLists(None, ListNode(0))) == [0]
#     assert to_list(sol.mergeTwoLists(ListNode(-1, ListNode(0)), ListNode(2, ListNode(3)))) == [-1, 0, 2, 3]
#     assert to_list(sol.mergeTwoLists(ListNode(1, ListNode(3, ListNode(5))), ListNode(2, ListNode(4)))) == [1, 2, 3, 4, 5]










