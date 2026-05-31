

class Solution:
    def getLongestSubsequence(self, words: list, groups: list) -> list:
        # Time: O(n)
        # Space: O(n)
        prev = groups[0]
        out = [words[0]]
        for i in range(1, len(groups)):
            if prev != groups[i]:
                out.append(words[i])
            prev = groups[i]
        return out


