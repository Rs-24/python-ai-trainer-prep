# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/increasing-decreasing-string/description/

class Solution:
    def sortString(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1
        res = []
        while len(res) < len(s):
            for i in range(26):
                if count[i] > 0:
                    res.append(chr(ord("a") + i))
                    count[i] -= 1
            for i in range(25, -1, -1):
                if count[i] > 0:
                    res.append(chr(ord("a") + i))
                    count[i] -= 1
        return "".join(res)


