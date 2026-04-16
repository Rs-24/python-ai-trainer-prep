# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/number-of-different-integers-in-a-string/description/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Time: O(n), n = len(word)
        # Space: O(n)
        ints = set()
        cur = 0
        in_number = False
        for ch in word:
            if ch.isdigit():
                cur = cur * 10 + int(ch)
                in_number = True
            else:
                if in_number:
                    ints.add(cur)
                    cur = 0
                    in_number = False
        if in_number:
            ints.add(cur)
        return len(ints)


