# Time to write all of below including tests, explanation and time and aux
# and total space: 25 mins

# Problem: https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0] * 26
        for ch in s1:
            count1[ord(ch) - ord("a")] += 1
        count2 = [0] * 26
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord("a")] += 1
        for i in range(len(s2) - len(s1) + 1):
            if count1 == count2:
                return True
            count2[ord(s2[i]) - ord("a")] -= 1
            if i + len(s1) > len(s2) - 1:
                break
            count2[ord(s2[i + len(s1)]) - ord("a")] += 1
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.checkInclusion("a", "a") == True
    assert sol.checkInclusion("a", "b") == False
    assert sol.checkInclusion("ab", "a") == False
    assert sol.checkInclusion("ab", "wsadb") == False
    assert sol.checkInclusion("ab", "wsabd") == True
    assert sol.checkInclusion("ab", "wsbad") == True

# Explanation: the code stores the count of s1 and s2, and iterates over s2
# while adjusting the count for s2 and checking if it equals the count for
# s1
# Time: O(n + m), n = len(s1), m = len(s2)
# Space: O(26) = O(1)


