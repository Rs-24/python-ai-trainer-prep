

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # Time: O(1)
        # Space: O(1)
        current = int(current[:2]) * 60 + int(current[3:])
        correct = int(correct[:2]) * 60 + int(correct[3:])
        diff = (correct - current) % 1440
        count = 0
        for m in [60, 15, 5, 1]:
            count += diff // m
            diff %= m
        return count


