

class Solution:
    def carFleet(self, target: int, position: list, speed: list) -> int:
        # Time: O(n log n)
        # Space: O(n)
        t = sorted(zip(position, speed), reverse=True)
        s = []
        for a, b in t:
            if not s or (target - a) / b > s[-1]:
                s.append((target - a) / b)
        return len(s)


