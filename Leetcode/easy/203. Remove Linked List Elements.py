# Time to write all of below including tests, explanation and time and aux
# and total space: 32 mins

# Problem: https://leetcode.com/problems/remove-linked-list-elements/description/

from typing import Optional, List, Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

def build(nums: List[int], x: int) -> Tuple[Optional[ListNode], List[int]]:
    dummy = ListNode()
    tail = dummy
    out = []
    for num in nums:
        tail.next = ListNode(num)      
        tail = tail.next
        if num != x:
            out.append(num)
    return dummy.next, out

def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    sol = Solution()
   
    linked_list, expected = build([], 3)
    assert to_list(sol.removeElements(linked_list, 3)) == expected

    linked_list, expected = build([1], 3)
    assert to_list(sol.removeElements(linked_list, 3)) == expected

    linked_list, expected = build([3], 3)
    assert to_list(sol.removeElements(linked_list, 3)) == expected

    linked_list, expected = build([1, 2, 3, 4], 3)
    assert to_list(sol.removeElements(linked_list, 3)) == expected

    linked_list, expected = build([3, 3, 3, 3], 3)
    assert to_list(sol.removeElements(linked_list, 3)) == expected

    linked_list, expected = build([1, 2, 3, 4], 0)
    assert to_list(sol.removeElements(linked_list, 0)) == expected

# Explanation: the code iterates through the list and skips nodes with values
# equal to val via cur.next = cur.next.next
# Time (of removeElements()) only: O(n), n = number of nodes in linked list
# Space (of removeElements()) only: excluding output: O(1)

# Recursive method:
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Time: O(n), n = number of nodes in linked list
        # Space, excluding output: O(n) due to recursion stack
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

# No dummy node method:
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Time only: O(n), n = number of nodes in linked list
        # Space only: excluding output: O(1)
        while head and head.val == val:
            head = head.next
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# Creating a new list method:
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Time: O(n), n = number of elements in list
        # Space, excluding output: O(1)
        dummy = ListNode()
        tail = dummy
        while head:
            if head.val != val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return dummy.next

# prev and cur pointer method:
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Time: O(n), n = number of nodes in list
        # Space, excluding output: O(1)
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next


