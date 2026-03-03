# Time to write all of below including tests, explanation and time and aux
# and total space: 15 mins

# Problem: https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        out = []
        syms = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        while num > 0:
            i = len(nums) - 1
            while i >= 0:
                if num >= nums[i]:
                    out.append(syms[nums[i]])
                    num -= nums[i]
                    break
                i -= 1
        return "".join(out)

if __name__ == "__main__":
    sol = Solution()
    assert sol.intToRoman(1) == "I"
    assert sol.intToRoman(2) == "II"
    assert sol.intToRoman(4) == "IV"
    assert sol.intToRoman(10) == "X"
    assert sol.intToRoman(231) == "CCXXXI"
    assert sol.intToRoman(1994) == "MCMXCIV"

# Explanation: the code stores a dictionary of numbers and their roman numeral
# counterparts, and appends the relevant numerals to out until num becomes zero
# Time: O(1)
# Space: excluding output: O(1)


