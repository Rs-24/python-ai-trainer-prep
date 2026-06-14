


class Solution:
    def minimumBoxes(self, apple: list, capacity: list) -> int:
        # Time: O(n log n)
        # Space: O(n)
        a = sum(apple)
        capacity.sort(reverse=True)
        t = 0
        for i, c in enumerate(capacity):
            t += c
            if t >= a:
                return i + 1


