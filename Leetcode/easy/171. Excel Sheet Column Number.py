# Time to write all of below including tests, explanation and time and aux 
# space: 13 mins

# Problem: https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:   
        total = 0
        for ch in columnTitle:
            total = total * 26 + ord(ch) - ord("A") + 1
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

# Explanation: the code iterates through the string, and each time multiplies 
# total by 26 and adds the corresponding number of the current character
# Time: O(n), n = len(columnTitle)
# Space: O(1)
        

