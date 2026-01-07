# Time to write all of below including tests, why the solution works and time 
# and space complexity: 3h 53 mins

# I couldn't figure this one out for some reason, and I required help from
# chatGPT to solve it

# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

from typing import List, Callable

class node:
    def __init__(self, given_val = None, given_next = None):
        self.val = given_val
        self.next = given_next

class LinkedList:
    def __init__(self):
        self.head = None

    def build_list(self, ll):
        if not ll:
            head = self.head = None
            return head
        else:
            cur = head = node(ll[0])
            for n in ll[1:]:
                cur.next = node(n)
                cur = cur.next
            self.head = head
            return head
        
    def revert_list(self, head):
        if not head:
            return_val: List[int] = []
            return return_val
        else:
            reverted_list: List[int] = []
            cur = head
            while cur:
                reverted_list.append(cur.val)
                cur = cur.next
            return reverted_list

    def remove_duplicates(head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
    
def run_tests(f: Callable) -> None:
    tests = [([1, 2], [1, 2]), ([], []), ([-1, -1, 3, 4], [-1, 3, 4]), ([0, 1, 3, 3], [0, 1, 3])]
    for test, expected in tests:
        ll_1 = LinkedList()
        actual = f(ll_1.build_list(test))
        reverted = ll_1.revert_list(actual)
        assert reverted == expected, f"{f.__name__}({test}) = {reverted}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_tests(LinkedList.remove_duplicates)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - The Node and LinkedLink classes are created. Within the LinkedList class, 
#     the relevant helper functions are created: build_list() to convert a 
#     standard Python list into a linked list, and revert_list() for the opposite
#     operation. Then the remove_duplicates function is created which iterates 
#     through the list and if the next value is equal to the current value, skips
#     that value
#
# Time complexity: O(n) where n is the length of the inputted list
# Space complexity: O(n) where n is the length of the inputted list
#
# Learning lessons (done after completing all of above in 3h 53 mins):
#   - The node class should actually be Node, because in the Leetcode problem page
#     the n is capitalized
#   - remove_duplicates() doesn't take in self as a parameter and hence is a
#     static method. Therefore I should have included @staticmethed above it
#   - Instead of doing: 'head = self.head = None', it might be better to change
#     it to 'self.head = None', and then return None

