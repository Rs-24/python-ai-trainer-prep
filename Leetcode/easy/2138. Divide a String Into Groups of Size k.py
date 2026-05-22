

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list:
        # Time: O(n)
        # Space: O(n)
        out = []
        for i in range(0, len(s), k):
            temp = s[i:i + k]
            if len(temp) < k:
                temp += fill * (k - len(temp))
            out.append(temp)
        return out


