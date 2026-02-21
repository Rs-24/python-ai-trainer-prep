# Time to write all of below including tests, explanation and time and aux 
# space: 15 mins

# Problem: https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l <= r and not s[l].lower().isalnum():
                l += 1
            while l <= r and not s[r].lower().isalnum():
                r -= 1
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(" ") == True
    assert sol.isPalindrome("1") == True
    assert sol.isPalindrome("a") == True
    assert sol.isPalindrome("racecar") == True
    assert sol.isPalindrome("R,a ce car") == True
    assert sol.isPalindrome("racecars") == False

# Explanation: the code uses two pointers at either end that move towards each
# other, and skips characters that aren't letters or numbers, and checks if the
# characters at the two pointers are equal
# Time: O(n), n = len(s)
# Space: O(1)

# Learning lessons (done after completing all of above in 15 mins):
#   - No major learning lessons




