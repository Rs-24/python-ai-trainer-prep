# Time to write all of below including tests, explanation and time and aux 
# space: 11 mins

# Problem: https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for ch in s:
            if ch.isalnum():
                s_list.append(ch.lower())
        return s_list == s_list[::-1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(",") == True
    assert sol.isPalindrome(" ") == True
    assert sol.isPalindrome("1") == True
    assert sol.isPalindrome("2") == True
    assert sol.isPalindrome("r a cec ar") == True
    assert sol.isPalindrome("r, acecar") == True
    assert sol.isPalindrome("race a car") == False

# Explanation: each alphanumeric character is converted to lowercase and 
# added to a list. At the end the list is checked if it equals its reversed
# counterpart
# Time: O(n), n = len(s)
# Aux space excluding output and input: O(n)
# Total space excluding output, including input: O(n)

# Learning lessons (done after completing all of above in 11 mins):
#   - It would be useful to know 


def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    l, r = 0, len(s)-1
    while l < r:
        while not s[l].isalnum():
            l += 1
        while not s[r].isalnum():
            r -= 1
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


         











