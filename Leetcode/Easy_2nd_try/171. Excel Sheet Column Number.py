# Time to write all of below including tests, explanation and time and aux 
# space: 13 mins

# Problem: https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        num = 0
        level = 0
        i = len(columnTitle) - 1
        while i >= 0:
            num = ord(columnTitle[i]) - ord("A") + 1
            num *= (26 ** (level))
            total += num
            level += 1
            i -= 1
        return total

if __name__ == "__main__":
    sol = Solution()
    assert sol.titleToNumber("A") == 1
    assert sol.titleToNumber("B") == 2
    assert sol.titleToNumber("Z") == 26
    assert sol.titleToNumber("AA") == 27
    assert sol.titleToNumber("AB") == 28
    assert sol.titleToNumber("AZ") == 52
    assert sol.titleToNumber("BA") == 53
    assert sol.titleToNumber("BB") == 54

# Explanation: the code iterates through the string from the end, and finds
# the corresponding number of the current character, multiplies it by the
# appropriate power of 26 and adds this to total
# Time: O(n), n = len(columnTitle)
# Space: O(1)

# Learning lessons (done after completing all of above in 13 mins):
#   - I now realise my solution can be simplified. My rewrite is below:
#
# def titleToNumber(self, columnTitle: str) -> int:
#     # Time: O(n), n = len(columnTitle)
#     # Space: O(1)
#     total = 0
#     for ch in columnTitle:
#         total = total * 26 + ord(ch) - ord("A") + 1
#     return total










