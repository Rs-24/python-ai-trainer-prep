# Time to write all of below including tests, explanation and time and aux 
# space: 11 mins

# Problem: https://leetcode.com/problems/linked-list-cycle/description/

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

# Tests:
# [] -> False
# [1] -> False
# [1, [back to 1]] -> True
# [0, -1, 2, [back to -1]] -> True

# Explanation: the function iterates through the linked list and checks if
# each node is in the seen set
# Time: O(n), n = number of nodes in the linked list
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 11 mins):
#   - I now realise there is also an O(1) space version. My rewrite is below:
#
# def hasCycle(self, head: Optional[ListNode]) -> bool:
#     # Time: O(n), n = number of nodes in linked list
#     # Aux space excluding output and input: O(1)
#     # Total space including output, excluding input: O(1)
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow is fast:
#             return True
#     return False
#
#   - Additionally, I could have improved my tests a bit. My rewrite is below:
#
# from typing import List
# def build_list(nums: List[int], pos: int) -> Optional[ListNode]:
#     dummy = ListNode(0)
#     tail = dummy
#     cycle_node = None
#     for i, num in enumerate(nums):
#         tail.next = ListNode(num)
#         tail = tail.next
#         if i == pos:
#             cycle_node = tail
#     if pos != -1 and nums:
#         tail.next = cycle_node
#     return dummy.next
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.hasCycle(build_list([], -1)) == False
#     assert sol.hasCycle(build_list([1], -1)) == False
#     assert sol.hasCycle(build_list([1], 0)) == True
#     assert sol.hasCycle(build_list([-1, 0, 1], 1)) == True
#     assert sol.hasCycle(build_list([-1, 0, 1, 2 ,3], -1)) == False
















