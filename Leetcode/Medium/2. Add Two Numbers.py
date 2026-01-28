# Time to write all of below including tests, explanation and time and aux
# and total space: 26 mins

# Problem: https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        level = 0
        while l1:
            n1 += l1.val * (10**level)
            level += 1
            l1 = l1.next
        n2 = 0
        level = 0
        while l2:
            n2 += l2.val * (10**level)
            level += 1
            l2 = l2.next
        total = n1 + n2
        if total == 0:
            return ListNode(0)
        head = ListNode()
        node = head
        while total > 0:
            node.next = ListNode(total % 10)
            total //= 10
            node = node.next
        return head.next

if __name__ == "__main__":
    sol = Solution()

    result = sol.addTwoNumbers(ListNode(1), ListNode(2))
    assert result.val == 3

    result = sol.addTwoNumbers(ListNode(0), ListNode(0))
    assert result.val == 0

    result = sol.addTwoNumbers(ListNode(1, ListNode(3)), ListNode(2))
    assert result.val == 3
    assert result.next.val == 3

    result = sol.addTwoNumbers(ListNode(1, ListNode(2)), ListNode(0, ListNode(3)))
    assert result.val == 1
    assert result.next.val == 5

    result = sol.addTwoNumbers(ListNode(1, ListNode(2, ListNode(4))), ListNode(5, ListNode(3, ListNode(2))))
    assert result.val == 6
    assert result.next.val == 5
    assert result.next.next.val == 6

# Explanation: the code iterates through each linked list to find n1 and n2. Then
# it finds the total and creates a new linked list from back to front
# representing the digits in total. Then it returns the head of this new linked
# list
# Time: O(n + m), n, m = number of nodes in each linked list respectively
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 26 mins):
#   - I now realise my solution can be simplified. My rewrite is below:
#
# def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     # Time: O(n), n = max(num_nodes(l1), num_nodes(l2))
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(n)
#     dummy = ListNode()
#     node = dummy
#     carry = 0
#     while l1 or l2 or carry:
#         x = l1.val if l1 else 0
#         y = l2.val if l2 else 0
#         total = x + y + carry
#         carry = total // 10
#         node.next = ListNode(total % 10)
#         node = node.next
#         l1 = l1.next if l1 else l1
#         l2 = l2.next if l2 else l2
#     return dummy.next
#
#   - Additionally, my tests could have been improved. My rewrite is below:
#
# if __name__ == "__main__":
#     sol = Solution()
#    
#     l1 = ListNode(1)
#     l2 = ListNode(2)    
#     result = sol.addTwoNumbers(l1, l2)
#     assert result.val == 3
#
#     l1 = ListNode(1)
#     l2 = ListNode(9, ListNode(9))    
#     result = sol.addTwoNumbers(l1, l2)
#     assert result.val == 0
#     assert result.next.val == 0
#     assert result.next.next.val == 1
#
#     l1 = ListNode(0)
#     l2 = ListNode(0)
#     result = sol.addTwoNumbers(l1, l2)
#     assert result.val == 0
#    
#     l1 = ListNode(0, ListNode(2))
#     l2 = ListNode(8, ListNode(3))    
#     result = sol.addTwoNumbers(l1, l2)
#     assert result.val == 8
#     assert result.next.val == 5
#
#     l1 = ListNode(1, ListNode(3, ListNode(6)))
#     l2 = ListNode(2, ListNode(9, ListNode(4)))
#     result = sol.addTwoNumbers(l1, l2)
#     assert result.val == 3
#     assert result.next.val == 2
#     assert result.next.next.val == 1
#     assert result.next.next.next.val == 1












