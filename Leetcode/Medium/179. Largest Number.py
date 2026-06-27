

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list) -> str:
        # Time: O(n^2)
        # Space: O(n)
        s = list(map(str, nums))
        def c(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0
        s.sort(key=cmp_to_key(c))
        out = "".join(s)
        return "0" if out[0] == "0" else out


