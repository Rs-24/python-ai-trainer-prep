# Time to write all of below including tests, explanation and time and aux 
# space: 1h 18 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/intersection-of-two-linked-lists/description/

from typing import Optional, List, Tuple

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

def build(listA: List[int], listB: List[int], skipA: int, skipB: int) -> Tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
    dummy_a = ListNode(0)
    tail_a = dummy_a
    a_nodes = []
    intersection_node = None
    for num_a in listA:
        tail_a.next = ListNode(num_a)
        tail_a = tail_a.next
        a_nodes.append(tail_a)
    if skipA != len(a_nodes):
        intersection_node = a_nodes[skipA]
    dummy_b = ListNode(0)
    tail_b = dummy_b
    for i in range(skipB):
        tail_b.next = ListNode(listB[i])
        tail_b = tail_b.next
    tail_b.next = intersection_node
    return dummy_a.next, dummy_b.next, intersection_node

if __name__ == "__main__":
    sol = Solution()

    a, b, expected = build([1], [1], 0, 0)
    assert sol.getIntersectionNode(a, b) == expected

    a, b, expected = build([2], [1, 2], 0, 1)
    assert sol.getIntersectionNode(a, b) == expected

    a, b, expected = build([1, 4, 7, 10], [2, 7, 10], 2, 1)
    assert sol.getIntersectionNode(a, b) == expected

    a, b, expected = build([1, 4, 7, 10], [1, 4, 7, 10], 0, 0)
    assert sol.getIntersectionNode(a, b) == expected

    a, b, expected = build([1, 4, 7, 10], [3, 4, 10], 3, 2)
    assert sol.getIntersectionNode(a, b) == expected

    a, b, expected = build([1, 4, 7, 10], [2, 3, 5], 4, 3)
    assert sol.getIntersectionNode(a, b) == expected

# Explanation: the code iterates through both lists until both pointers are
# equal, and once it reaches the end of one list, moves on to the start of
# the other list. If the lists intersect, then the intersecting node will be
# reached, and if not, then None will be reached by both lists at the same
# time
# Time: O(m + n)
# Space: O(1)

# Learning lessons (done after completing all of above in 1h 18 mins):
#   - Another method would be using a set, my attempt is below:
#
# def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#     # Time: O(m + n), m, n = number of nodes in each listA, listB, respectively
#     # Space: O(m)
#     seen = set()
#     nodeA = headA
#     while nodeA:
#         seen.add(nodeA)
#         nodeA = nodeA.next
#     nodeB = headB
#     while nodeB:
#         if nodeB in seen:
#             return nodeB
#         nodeB = nodeB.next
#     return None









