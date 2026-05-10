

class Solution:
    def isHappy(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        def next_num(x: int) -> int:
            nxt = 0
            while x > 0:
                nxt += (x % 10)**2
                x //= 10
            return nxt
        slow = fast = n
        while True:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
            if slow == fast:
                break
        return slow == 1


