# Time to write all of below including tests, explanation and time and aux
# and total space: 50 mins

# Problem: https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        out = []
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        while num > 0:
            i = len(numbers) - 1
            while i >= 0:
                sym_num = numbers[i]
                if sym_num <= num:
                    num -= sym_num
                    out.append(symbols[sym_num])
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
# counterpart, and appends the relevant numerals to out until num becomes zero
# Time: O(d), d = number of digits in num
# Aux space, excluding output and input: O(d)
# Total space, including output, excluding input: O(d)

# Learning lessons (done after completing all of above in 50 mins):
#   - I now realise my complexity comments can be improved. My rewrite is below: 
#
# Time: O(13*k) = O(k), k = number of symbols appended to out 
# Aux space, excluding output and input (assuming out variable counts as output space): O(1)
# Total space, including output, excluding input: O(k)










