# Time to write all of below including tests, why the solution works and time 
# and space complexity: 33 mins

# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        node = None
        while head:
            if not head.next:
                break
            node = head
            while node.next and node.val == node.next.val:
                node = node.next
            head.next = node.next
            head = head.next        
        return dummy.next

def build_listnodes(nums: list) -> Optional[ListNode]:
    if not nums:
        return
    dummy = ListNode()
    tail = dummy
    for num in nums:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next

def convert_to_list(head: Optional[ListNode]) -> list:
    if not head:
        return []
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    sol = Solution()

    l1 = build_listnodes([])
    out = sol.deleteDuplicates(l1)
    assert convert_to_list(out) == []

    l1 = build_listnodes([1])
    out = sol.deleteDuplicates(l1)
    assert convert_to_list(out) == [1]

    l1 = build_listnodes([1, 2, 2, 3, 4, 4])
    out = sol.deleteDuplicates(l1)
    assert convert_to_list(out) == [1, 2, 3, 4]

    l1 = build_listnodes([-1, -1, 0, 1, 2, 2])
    out = sol.deleteDuplicates(l1)
    assert convert_to_list(out) == [-1, 0, 1, 2]

# Explanation: the code iterates through the linked list, and uses a while
# loop to skip over duplicate nodes
# Time (of deleteDuplicates() only): worst case O(n) if linked list has no
# duplicates, n = number of nodes in linked list
# Aux space, excluding output and input (of deleteDuplicates() only): O(1)
# Total space, including output, excluding input: O(1)


