

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # Time: O(m + n), m = len(list1), n = len(list2)
        # Space: O(m + n)
        d = {word: i for i, word in enumerate(list1)}
        best = float("inf")
        out = []
        for i, word in enumerate(list2):
            if word in d:
                if i + d[word] < best:
                    out = [word]
                    best = i + d[word]
                elif i + d[word] == best:
                    out.append(word)
        return out


