# 203

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

    def remove_duplicates(head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
    
def run_tests(f: Callable) -> None:
    tests = [([1, 2], [1, 2]), ([], None), ([-1, -1, 3, 4], [-1, 3, 4]), ([0, 1, 3, 3], [0, 1, 3])]
    for test, expected in tests:
        print(test)
        ll_1 = LinkedList()
        actual = f(ll_1.build_list(test))
        ll_2 = LinkedList()
        assert actual == ll_2.build_list(expected), f"{f.__name__}({test}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_tests(LinkedList.remove_duplicates)
    print("All tests passed!")

if __name__ == "__main__":
    test()




