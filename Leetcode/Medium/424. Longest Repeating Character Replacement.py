# Time to write all of below including tests, explanation and time and aux
# and total space: 1h 19 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        best = 0
        max_count = 0
        for r, ch in enumerate(s):
            idx = ord(ch) - ord("A")
            count[idx] += 1
            max_count = max(max_count, count[idx])
            while max_count + k < r - l + 1:
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
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 1h 19 mins):
#   - No major learning lessons





