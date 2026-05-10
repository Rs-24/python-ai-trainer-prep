
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(n), n = len(s) = len(t)
        # Space: O(1)
        if len(s) != len(t):
            return False
        count = [0] * 26
        for ch1, ch2 in zip(s, t):
            count[ord(ch1) - ord("a")] += 1
            count[ord(ch2) - ord("a")] -= 1
        return all(c == 0 for c in count)


