

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # Time: O(n * k)
        # Space: O(k)
        count = 0
        for i in range(len(str(num)) - k + 1):
            cur = int(str(num)[i:i + k])
            if cur != 0 and num % cur == 0:
                count += 1
        return count


