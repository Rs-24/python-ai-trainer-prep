

class Solution:
    def countConsistentStrings(self, allowed: str, words: list) -> int:
        # Time: O(m + n), m = len(allowed), n = total number of characters in
        # words
        # Space: O(m) 
        a = set(allowed)
        count = 0
        for word in words:
            valid = 1
            for ch in word:
                if ch not in a:
                    valid = 0
                    break
            count += valid
        return count


