

class Solution:
    def maximum69Number(self, num: int) -> int:
        # Time: O(n), n = len(num)
        # Space: O(n)
        return int(str(num).replace("6", "9", 1))


