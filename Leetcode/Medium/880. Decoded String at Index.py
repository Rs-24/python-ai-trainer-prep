

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # Time: O(n)
        # Space: O(1)
        t = 0
        for ch in s:
            if ch.isdigit():
                t *= int(ch)
            else:
                t += 1
        for i in range(len(s) - 1, -1, -1):
            k %= t
            if s[i].isalpha():
                if k == 0:
                    return s[i]
                t -= 1
            else:
                t //= int(s[i])


