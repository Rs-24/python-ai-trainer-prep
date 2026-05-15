

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        # Time: O(n + log k), n = len(num)
        # Space: O(n)
        i = len(num) - 1
        out = []
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
            out.append(k % 10)
            k //= 10
            i -= 1
        return list(reversed(out))


