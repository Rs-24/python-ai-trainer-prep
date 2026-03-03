# Time to write all of below including tests, explanation and time and aux
# and total space: 29 mins

# Problem: https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        best = 0
        for r, ch in enumerate(s):
            count[ord(ch) - ord("A")] += 1
            while max(count) + k < r - l + 1:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best

if __name__ == "__main__":
    sol = Solution()
    assert sol.characterReplacement("A", 0) == 1
    assert sol.characterReplacement("B", 1) == 1
    assert sol.characterReplacement("ABC", 0) == 1
    assert sol.characterReplacement("ABC", 1) == 2
    assert sol.characterReplacement("ABC", 2) == 3
    assert sol.characterReplacement("ABC", 3) == 3
    assert sol.characterReplacement("ABAB", 1) == 3
    assert sol.characterReplacement("ABAB", 2) == 4

# Explanation: the code iterates over s using a sliding window, while constantly
# monitoring the most frequent character in the current window to see if the 
# current window can produce the longest repeating character substring
# Time: O(n), n = len(s)
# Space: O(26) = 0(1)


