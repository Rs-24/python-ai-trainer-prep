

class Solution:
    def convertTemperature(self, celsius: float) -> list:
        # Time: O(1)
        # Space: O(1)
        return [celsius + 273.15, celsius * 1.8 + 32]


