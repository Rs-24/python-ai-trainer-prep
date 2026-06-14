

class Solution:
    def trafficSignal(self, timer: int) -> str:
        # Time: O(1)
        # Space: O(1)
        return "Green" if timer == 0 else "Orange" if timer == 30 else "Red" if 30 < timer <= 90 else "Invalid"


