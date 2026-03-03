# Time to write all of below including tests, explanation and time and aux
# and total space: 13 mins

# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in seen and left <= seen[ch]:
                left = seen[ch] + 1
            seen[ch] = right
            best = max(best, right - left + 1)
        return best

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring("a") == 1
    assert sol.lengthOfLongestSubstring("aa") == 1
    assert sol.lengthOfLongestSubstring("Aa") == 2
    assert sol.lengthOfLongestSubstring("abc c") == 4
    assert sol.lengthOfLongestSubstring("  ") == 1
    assert sol.lengthOfLongestSubstring("hello") == 3
    assert sol.lengthOfLongestSubstring("Hi1231") == 5
    assert sol.lengthOfLongestSubstring("12345") == 5
    assert sol.lengthOfLongestSubstring("1 2 ") == 3

# Explanation: the code uses a left and right pointer with a seen dictionary
# and a best variable to determine the longest substring, and once the loop
# ends best is returned
# Time: O(n), n = len(s)
# Space: O(k), k = number of unique characters, worst case O(n)

# set method:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: worst case O(n)
        seen = set()
        left = 0
        best = 0
        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            best = max(best, right - left + 1)
        return best


