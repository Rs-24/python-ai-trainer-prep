# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/truncate-sentence/description/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(n)
        s = s.split()
        return " ".join(s[:k])


