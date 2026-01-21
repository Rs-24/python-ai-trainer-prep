# Time to write all of below including tests, explanation and time and aux 
# space: 35 mins

# Problem: https://leetcode.com/problems/intersection-of-two-linked-lists/description/

from typing import Optional, Tuple, List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = [], []

        node = headA
        while node:
            a.append(node)
            node = node.next

        node = headB
        while node:
            b.append(node)
            node = node.next

        for node in a:
            if node in b:
                return node
        return None

def build(listA: List[int], listB: List[int], intersectVal: int, skipA: int, skipB: int) -> Tuple[ListNode, ListNode]:
    headA = ListNode(listA[0])
    headB = ListNode(listB[0])

    link_node = None

    nodeA = headA.next
    nodeB = headB.next

    for i, num in enumerate(listA):
        if i == 0:
            continue
        if num == intersectVal:
            break
        nodeA = ListNode(num)
        nodeA = nodeA.next

    for i, num in enumerate(listB):
        if i == 0:
            continue
        nodeB = ListNode(num)
        if num == intersectVal:
            link_node = nodeB
        nodeB = nodeB.next

    if intersectVal > 0:
        nodeA = link_node

    return headA, headB

if __name__ == "__main__":
    sol = Solution()
    
    a, b = build([1], [2], 0, 0, 0)
    assert sol.getIntersectionNode(a, b) ==  None

    a, b = build([1, 2, 3], [2, 3], 2, 1, 0)
    assert sol.getIntersectionNode(a, b) == a.next
    
    a, b = build([1, 2, 3], [4, 5, 6], 0, 0, 0)
    assert sol.getIntersectionNode(a, b) == None

# Explanation: Each tree is converted to a list and the first element in each
# list that are equal is returned
# Time: O(n * m), n, m = number of nodes in each tree respectively
# Aux space, excluding output and input (of def getIntersectionNode() only): O(n + m)
# Total space, including output, excluding input (of def getIntersectionNode() only): O(n + m)

# Learning lessons (done after completing all of above in 35 mins):
#   - In retrospect my solution is a bit inefficient, and there is a way to do
#     it in O(n + m) time, where n, m = number of nodes in listA and listB
#     respectively. My attempt is below:
#
# def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#     # Time: O(n + m), n, m = number of nodes in listA and listB respectively
#     # Aux space, excluding output and input: O(n), n = number of nodes in listA
#     # Total space, including output, excluding input: O(n)
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
#
#   - Additionally, I now realise there is a version with no extra space. As
#     such, my attempt is below:
#
# def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#     # Time: O(n + m), n, m = number of nodes in listA and listB respectively
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     a, b = headA, headB
#     while a is not b:
#         a = a.next if a else headB
#         b = b.next if b else headA
#     return a







