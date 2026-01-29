# Time to write all of below including tests, explanation and time and aux
# and total space: 13 mins

# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = []
        for ch in s:
            if ch in substring:
                longest = max(longest, len(substring))
                substring = [ch]
            else:
                substring.append(ch)
        return max(longest, len(substring))

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

# Explanation: the function stores the current substring in the substring list,
# and iterates through each character in s and adjusts substring and longest
# as it goes along. At the end, max(longest, len(substring)) is returned
# Time: O(n), n = len(s)
# Aux space, excluding output and input: worst case O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 13 mins):
#   - I now realise my solution is incorrect. My rewrite is below:
#
# def lengthOfLongestSubstring(self, s: str) -> int:
#     # Time: O(n), n = len(s)
#     # Aux space, excluding output and input: worst case O(min(n, k)),
#     # k = total number of allowed characters
#     # Total space, including output, excluding input: worst case O(min(n, k))
#     left = 0
#     longest = 0
#     seen = {}
#     for right, ch in enumerate(s):
#         if ch in seen and left <= seen[ch]:
#             left = seen[ch] + 1
#         seen[ch] = right
#         longest = max(longest, right-left+1)    
#     return longest
#
#   - Additionally, there is also a method using a set, my attempt is below:
#
# def lengthOfLongestSubstring(self, s: str) -> int:
#     # Time: O(n), n = len(s)
#     # Aux space, excluding output and input: worst case O(min(n, k)), k = total
#     # number of allowed characters
#     # Total space, including output, excluding input: O(min(n, k))
#     seen = set()
#     left = 0
#     best = 0
#     for right, ch in enumerate(s):
#         while ch in seen:
#             seen.remove(s[left])
#             left += 1
#         seen.add(ch)
#         best = max(best, right-left+1)
#     return best
























