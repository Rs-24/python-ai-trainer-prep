

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Time: O(n)
        # Space: O(n)
        while len(s) > k:
            d = []
            for i in range(0, len(s), k):
                d.append(str(sum(int(d) for d in s[i:i + k])))
            s = "".join(d)
        return s


