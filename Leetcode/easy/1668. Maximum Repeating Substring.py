# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/maximum-repeating-substring/description/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # Time: O(k * m), m = len(sequence)
        # Space: O(k * n), n = len(word)
        k = 0
        temp = word
        while temp in sequence:
            k += 1
            temp += word
        return k


