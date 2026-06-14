

class Solution:
    def minimumIndex(self, capacity: list, itemSize: int) -> int:
        # Time: O(n)
        # Space: O(1)
        b = -1
        for i, c in enumerate(capacity):
            if c >= itemSize:
                if b == -1 or c < capacity[b]:
                    b = i
        return b


