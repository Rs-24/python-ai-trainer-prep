# Time to write all of below including tests, explanation and time and aux
# and total space: 25 mins

# Problem: https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        count1 = [0] * 26
        for ch in s1:
            count1[ord(ch) - ord("a")] += 1
        for i in range(len(s2) - s1_len + 1):
            if s2[i] in s1:
                count2 = [0] * 26
                for j in range(s1_len):
                    ch = s2[i + j]
                    count2[ord(ch) - ord("a")] += 1
                if count1 == count2:
                    return True
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.checkInclusion("a", "a") == True
    assert sol.checkInclusion("a", "b") == False
    assert sol.checkInclusion("ab", "a") == False
    assert sol.checkInclusion("ab", "wsadb") == False
    assert sol.checkInclusion("ab", "wsabd") == True
    assert sol.checkInclusion("ab", "wsbad") == True

# Explanation: the code iterates through s2 and if the character is in s1,
# checks if the substring is a permutation of s1
# Time: O(n * m), n, m = len(s1), len(s2)
# Aux space, excluding output and input: O(26) = O(1)
# Total space, including output, excluding input: O(26) = O(1)

# Learning lessons (done after completing all of above in 25 mins):
#   - I now realise there is a linear time solution, my attempt is below: 
#
# def checkInclusion(self, s1: str, s2: str) -> bool:
#     # Time: O(n + m), n, m = len(s1), len(s2)
#     # Aux space, excluding output and input: O(26) = O(1)
#     # Total space, including output, excluding input: O(26) = O(1)
#     n, m = len(s1), len(s2)
#     if n > m:
#         return False
#     count1 = [0] * 26
#     for ch in s1:
#         count1[ord(ch) - ord("a")] += 1
#     count2 = [0] * 26
#     for i in range(n):
#         count2[ord(s2[i]) - ord("a")] += 1
#     if count1 == count2:
#         return True
#     for i in range(n, m):
#         count2[ord(s2[i-n]) - ord("a")] -= 1
#         count2[ord(s2[i]) - ord("a")] += 1
#         if count1 == count2:
#             return True
#     return False









