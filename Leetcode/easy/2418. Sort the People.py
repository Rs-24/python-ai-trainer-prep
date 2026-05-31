

class Solution:
    def sortPeople(self, names: list, heights: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        a = [(n, h) for n, h in zip(names, heights)]
        a.sort(key=lambda x: x[1], reverse=True)
        return [n for n, _ in a]


