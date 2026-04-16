# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/capitalize-the-title/description/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # Time: O(n), n = len(title)
        # Aux space: O(n)
        new = []
        for word in title.split():
            if len(word) <= 2:
                new.append(word.lower())
            else:
                chars = list(word.lower())
                chars[0] = chars[0].upper()
                new.append("".join(chars))
        return " ".join(new)


