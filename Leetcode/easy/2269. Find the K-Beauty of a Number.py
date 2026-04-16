# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # Time: O(d), d = number of digits in num 
        # Space: O(d)
        count = 0
        for i in range(0, len(str(num)) - k + 1):
            cur = str(num)[i:i + k]
            if cur[0] != "0" and num % int(cur) == 0:
                count += 1
        return count


