# 32 - 


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
        return longest








