

class Solution:
    def camelMatch(self, queries: list, pattern: str) -> list:
        # Time: O(n)
        # Space: O(n)
        def c(s: str) -> bool:
            i = 0
            for ch in s:
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                elif ch.isupper():
                    return False
            return i == len(pattern)
        return [c(q) for q in queries]


