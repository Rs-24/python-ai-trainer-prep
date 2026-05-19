

class Solution:
    def canBeEqual(self, target: list, arr: list) -> bool:
        # Time: O(m log m + n log n), m = len(target), n = len(target)
        # Space: O(m + n)
        return sorted(target) == sorted(arr)


