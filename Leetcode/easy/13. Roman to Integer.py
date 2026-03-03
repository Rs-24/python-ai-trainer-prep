# Time to write all of below including tests, why the solution works and time 
# and space complexity: 21 mins

# Problem: https://leetcode.com/problems/roman-to-integer/description/ 

class Solution:
    def romanToInt(self, s: str) -> int:
        ints = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev_ch = None
        for ch in s:
            total += ints[ch]
            if prev_ch is not None and ints[prev_ch] < ints[ch]:
                total -= (2 * ints[prev_ch])
            prev_ch = ch
        return total

if __name__ == "__main__":
    sol = Solution()
    assert sol.romanToInt("I") == 1
    assert sol.romanToInt("C") == 100
    assert sol.romanToInt("IV") == 4
    assert sol.romanToInt("MV") == 1005
    assert sol.romanToInt("MMLIV") == 2054

# Explanation: the code iterates through the string and converts each
# character to its integer counterpart while incrementing total, and if the
# current integer is greater than the previous integer, subtracts two of the
# previous integer from total
# Time: O(n), n = len(s)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)
    

