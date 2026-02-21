# Time to write all of below including tests, explanation and time and aux 
# space: 14 mins

# Problem: https://leetcode.com/problems/linked-list-cycle/description/

from typing import Optional, List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def build(nums: List[int], pos: int) -> Optional[ListNode]:
    if not nums:
        return None
    dummy = ListNode(0)
    cycle_node = None
    tail = dummy
    for i in range(len(nums)):
        tail.next = ListNode(nums[i])
        tail = tail.next
        if i == pos:
            cycle_node = tail
    if cycle_node is not None:
        tail.next = cycle_node
    return dummy.next

if __name__ == "__main__":
    sol = Solution()

    assert sol.hasCycle(None) == False

    head = build([1, 2, 3, 4], -1)
    assert sol.hasCycle(head) == False

    head = build([1, 2, 3, 4], 1)
    assert sol.hasCycle(head) == True

    head = build([-1, 0, 1], 0)
    assert sol.hasCycle(head) == True

    head = build([1, 2, 3, 4], 3)
    assert sol.hasCycle(head) == True

# Explanation: the code uses two pointers: fast and slow and if they are ever
# equal, returns True
# Time: O(n), n = number of nodes in list
# Space: O(1)

# Learning lessons (done after completing all of above in 14 mins):
#   - No major learning lessons



