# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/categorize-box-according-to-criteria/description/

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        # Time: O(1)
        # Space: O(1)
        b = any(d >= 10**4 for d in [length, width, height]) or (length * width * height) >= 10**9
        h = mass >= 100
        if b and h:
            return "Both"
        if b or h:
            return "Bulky" if b else "Heavy"
        return "Neither"


