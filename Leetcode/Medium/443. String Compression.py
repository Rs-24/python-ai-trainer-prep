

class Solution:
    def compress(self, chars: list) -> int:
        # Time: O(n)
        # Space: O(n1)
        n = len(chars)
        i = j = 0
        while i < n:
            t = 1
            while i < n - 1 and chars[i] == chars[i + 1]:
                i += 1
                t += 1
            chars[j] = chars[i]
            j += 1
            if t > 1:
                for d in str(t):
                    chars[j] = d
                    j += 1
            i += 1
        return j


