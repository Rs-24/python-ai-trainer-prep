# Time to write all of below including tests, explanation and time and aux 
# space: 14 mins

# Problem: https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{": "}", "[": "]", "(": ")"}
        opened = ""
        for ch in s:
            if ch in "{[(":
                opened += ch
            elif ch in ")]}":
                if opened == "":
                    return False
                if ch != pairs[opened[-1]]:
                    return False
                opened = opened[:len(opened)-1]
        return opened == ""

if __name__ == "__main__":
    sol = Solution()
    assert not sol.isValid("(")
    assert not sol.isValid("}")
    assert sol.isValid("(){}[]")
    assert sol.isValid("([{}])")
    assert not sol.isValid("(}){}")

# Explanation: The opened brackets are stored in the string open, and if open
# is empty once the loop ends then True is returned, otherwise False
# Time: O(len(s))
# Aux space: O(len(s))

# Learning lessons (done after completing all of above in 14 mins):
#   - Worst case time complexity should actually be O(len(s)^2) due
#     repeated string concatenation and slicing
#   - A stack would have been better than a string, and would have kept
#     the worst case time complexity as O(len(s))





