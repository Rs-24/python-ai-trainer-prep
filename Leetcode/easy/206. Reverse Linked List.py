# Time to write all of below including tests, explanation and time and aux
# and total space: 23 mins

# Problem: https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

def to_nodes(nums: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for num in nums:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next

def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    sol = Solution()
    assert to_list(sol.reverseList(to_nodes([]))) == []
    assert to_list(sol.reverseList(to_nodes([1]))) == [1]
    assert to_list(sol.reverseList(to_nodes([1, 2, 3]))) == [3, 2, 1]
    assert to_list(sol.reverseList(to_nodes([-1, -1, -1]))) == [-1, -1, -1]
    assert to_list(sol.reverseList(to_nodes([5, 3, 0]))) == [0, 3, 5]

# Explanation: the code uses a prev and cur pointers and iterates through the
# list while setting cur.next to prev, so that the list is reversed
# Time: O(n), n = number of elements in list
# Space, excluding output: O(1)

# Recursive method 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n), n = number of nodes in list
        # Space, excluding output: O(n) due to recursion stack
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


