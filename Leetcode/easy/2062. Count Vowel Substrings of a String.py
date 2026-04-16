# Time to write all of below including tests, explanation and time and aux
# and total space: 3 min

# Problem: https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # Time: O(n^2)
        # Space: O(1)
        vowels = set("aeiou")
        count = 0
        for i in range(len(word)):
            seen = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    count += 1
        return count


