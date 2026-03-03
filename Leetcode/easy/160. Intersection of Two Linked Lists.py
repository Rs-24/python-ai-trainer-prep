# Time to write all of below including tests, explanation and time and aux 
# space: 20 mins

# Problem: https://leetcode.com/problems/intersection-of-two-linked-lists/description/

from typing import Optional, List, Tuple

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

def build(listA: List[int], listB: List[int], skipA: int, skipB: int) -> Tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
    dummyA = ListNode(0)
    tail = dummyA
    intersection_node = None
    for i, num in enumerate(listA):
        tail.next = ListNode(num)
        if i == skipA:
            intersection_node = tail.next
        tail = tail.next
    dummyB = ListNode(0)
    tail = dummyB
    for i in range(skipB):
        tail.next = ListNode(listB[i])
        tail = tail.next
    tail.next = intersection_node
    return dummyA.next, dummyB.next, intersection_node

if __name__ == "__main__":
    sol = Solution()

    a, b, expected = build([1], [1], 0, 0)
    assert sol.getIntersectionNode(a, b) is expected

    a, b, expected = build([2], [1, 2], 0, 1)
    assert sol.getIntersectionNode(a, b) is expected

    a, b, expected = build([1, 4, 7, 10], [2, 7, 10], 2, 1)
    assert sol.getIntersectionNode(a, b) is expected

    a, b, expected = build([1, 4, 7, 10], [1, 4, 7, 10], 0, 0)
    assert sol.getIntersectionNode(a, b) is expected

    a, b, expected = build([1, 4, 7, 10], [3, 4, 10], 3, 2)
    assert sol.getIntersectionNode(a, b) is expected

    a, b, expected = build([1, 4, 7, 10], [2, 3, 5], 4, 3)
    assert sol.getIntersectionNode(a, b) is expected

# Explanation: the code iterates uses pointers a and b to iterate through both
# lists, and if it reaches the end of one list, moves to the beginnning of the
# next list. If the two lists intersect, the two pointers will meet at the
# intersecting node and that node is returned. If they don't intersect, then
# the two lists don't intersect, then both pointers will eventually reach None
# at the same time, and None is returned
# Time: O(m + n), m = number of nodes in listA, n = number of nodes in listB
# Space: excluding output: O(1)

# set method:
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # Time: O(m + n), m = number of nodes in listA, n = number of nodes in listB
    # Space: excluding output: O(m)
    seen = set()
    while headA:
        seen.add(headA)
        headA = headA.next    
    while headB:
        if headB in seen:
            return headB
        headB = headB.next
    return None


