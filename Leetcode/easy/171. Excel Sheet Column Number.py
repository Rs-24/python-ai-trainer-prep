# Time to write all of below including tests, explanation and time and aux 
# space: 21 mins

# Problem: https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        def num(s: str) -> int:
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for i, ch in enumerate(alphabet):
                if ch == s:
                    return i + 1
        digit = 0
        for letter in reversed(columnTitle):
            total += (num(letter) * (26 ** (digit)))
            digit += 1
        return total 

if __name__ == "__main__":
    sol = Solution()
    assert sol.titleToNumber("A") == 1
    assert sol.titleToNumber("B") == 2
    assert sol.titleToNumber("Z") == 26
    assert sol.titleToNumber("AA") == 27
    assert sol.titleToNumber("AB") == 28
    assert sol.titleToNumber("AY") == 51
    assert sol.titleToNumber("AZ") == 52
    assert sol.titleToNumber("BA") == 53
    assert sol.titleToNumber("BB") == 54
    assert sol.titleToNumber("ZY") == 701
    assert sol.titleToNumber("ZZ") == 702
    assert sol.titleToNumber("AAA") == 703
    assert sol.titleToNumber("AAB") == 704

# Explanation: columnTitle is reversed, and each corresponding letter is
# converted to a number, multiplied by the appropriate power of 26 and added
# to total. Once the loop ends, total is returned
# Time: O(26 * n), n = len(columnTitle)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 21 mins):
#   - I now realise my solution can be simplified. My rewrite is below:
#
# def titleToNumber(self, columnTitle: str) -> int:
#     # Time: O(n), n = len(columnTitle)
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     total = 0
#     for ch in columnTitle:
#         total = (total * 26) + (ord(ch) - ord("A") + 1)
#     return total







