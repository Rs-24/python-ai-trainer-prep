# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        nums = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                nums.append(int(s[i - 2:i]))
                i -= 3
            else:
                nums.append(int(s[i]))
                i -= 1
        letters = []
        i = len(nums) - 1
        while i >= 0:
            letters.append(chr(nums[i] + ord("a") - 1))
            i -= 1
        return "".join(letters)


