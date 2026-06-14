

class Solution:
    def letterCombinations(self, digits: str) -> list:
        # Time: O(n^2)
        # Space: O(n)
        c = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        out = []
        for d in digits:
            t = []
            for ch1 in out:
                for ch2 in c[d]:
                    t.append(ch1 + ch2)
            out = t
        return out


