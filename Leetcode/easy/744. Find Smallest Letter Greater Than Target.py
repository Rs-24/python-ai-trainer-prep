

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # Time: O(log n), n = len(letters)
        # Space:  O(1)
        l, r = 0, len(letters)
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return letters[l % len(letters)]


