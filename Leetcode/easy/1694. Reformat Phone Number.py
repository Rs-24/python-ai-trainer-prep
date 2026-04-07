# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/reformat-phone-number/description/

class Solution:
    def reformatNumber(self, number: str) -> str:
        # Time: O(n), n = len(number)
        # Space, excluding output: O(n)
        removed = []
        for ch in number:
            if ch.isdigit():
                removed.append(ch)
        letters = []
        while len(removed) > 4:
            letters.extend(removed[:3])
            letters.append("-")
            removed = removed[3:]
        if len(removed) <= 3:
            letters.extend(removed)
        else:
            letters.extend(removed[:2])
            letters.append("-")
            letters.extend(removed[2:])
        return "".join(letters)


