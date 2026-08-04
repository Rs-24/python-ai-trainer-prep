

class Solution:
    def reorderLogFiles(self, logs: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        def k(s: str) -> tuple:
            a, b = s.split(" ", 1)
            if b[0].isalpha():
                return (0, b, a)
            return (1, )
        return sorted(logs, key=k)


        