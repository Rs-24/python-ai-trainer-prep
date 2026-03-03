# Time to write all of below including tests, why the solution works and time 
# and space complexity: 25 mins

# Problem: https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        while i >= 0:
            if s[i] == " ":
                if length > 0:
                    return length
            else:
                length += 1
            i -= 1
        return length

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLastWord("I") == 1
    assert sol.lengthOfLastWord(" I ") == 1
    assert sol.lengthOfLastWord("hi") == 2
    assert sol.lengthOfLastWord("hi ") == 2
    assert sol.lengthOfLastWord(" hi") == 2
    assert sol.lengthOfLastWord(" hi  I  ") == 1

# Explanation: the code iterates through s from the end, and if a space is
# reached and length is greater than 0, then length is returned. Otherwise
# if a letter is reached, then length is incremented
# Time: worst case O(n) if s consists of only one word and no spaces,
# n = len(s)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

    
