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
        dummy = ListNode()
        tail = dummy
        carry = 0
        total = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            total = a + b + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return dummy.next

if __name__ == "__main__":
    sol = Solution()
   
    l1 = ListNode(1)
    l2 = ListNode(2)    
    result = sol.addTwoNumbers(l1, l2)
    assert result.val == 3

    l1 = ListNode(1)
    l2 = ListNode(9, ListNode(9))    
    result = sol.addTwoNumbers(l1, l2)
    assert result.val == 0
    assert result.next.val == 0
    assert result.next.next.val == 1

    l1 = ListNode(0)
    l2 = ListNode(0)
    result = sol.addTwoNumbers(l1, l2)
    assert result.val == 0
   
    l1 = ListNode(0, ListNode(2))
    l2 = ListNode(8, ListNode(3))    
    result = sol.addTwoNumbers(l1, l2)
    assert result.val == 8
    assert result.next.val == 5

    l1 = ListNode(1, ListNode(3, ListNode(6)))
    l2 = ListNode(2, ListNode(9, ListNode(4)))
    result = sol.addTwoNumbers(l1, l2)
    assert result.val == 3
    assert result.next.val == 2
    assert result.next.next.val == 1
    assert result.next.next.next.val == 1

# Explanation: the code iterates through both linked lists while summing each
# element with carry to build the new linked list
# Time: O(max(n1, n2)), n1 = number of nodes in l1, n2 = number of nodes in l2
# Space: excluding output: O(1)


