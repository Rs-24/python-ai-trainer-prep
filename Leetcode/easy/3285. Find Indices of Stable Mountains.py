

class Solution:
    def stableMountains(self, height: list, threshold: int) -> list:
        # Time: O(n)
        # Space: O(n)
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]


