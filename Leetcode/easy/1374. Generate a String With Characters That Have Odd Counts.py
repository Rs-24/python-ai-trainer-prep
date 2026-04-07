# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/description/

class Solution:
    def generateTheString(self, n: int) -> str:
        # Time: O(n)
        # Space: O(n)
        if n % 2 == 1:
            return "".join(["a"] * n)
        return "".join(["a"] + ["b"] * (n - 1))


