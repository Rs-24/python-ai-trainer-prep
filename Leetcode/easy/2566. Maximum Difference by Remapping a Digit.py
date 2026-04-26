# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/

class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Time: O(d), d = number of digits in num
        # Space: O(d)
        s = str(num)
        max_num = s
        for d in s:
            if d != "9":
                max_num = s.replace(d, "9")
                break
        min_num = s.replace(s[0], "0")
        return int(max_num) - int(min_num)


