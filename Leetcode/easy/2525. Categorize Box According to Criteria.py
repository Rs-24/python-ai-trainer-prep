

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        # Time: O(1)
        # Space: O(1)
        b = any(d >= 10**4 for d in [length, width, height]) or length * width * height >= 10**9
        h = mass >= 100
        if b and h:
            return "Both"
        if b or h:
            return "Bulky" if b else "Heavy"
        return "Neither"


