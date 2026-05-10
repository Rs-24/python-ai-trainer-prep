# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/generate-tag-for-video-caption/description/

class Solution:
    def generateTag(self, caption: str) -> str:
        # Time: O(n), n = len(caption)
        # Space: O(n)
        words = caption.split()
        res = []
        for word in words:
            clean = "".join(ch for ch in word if ch.isalpha())
            if not clean:
                continue
            if not res:
                res.append(clean.lower())
            else:
                res.append(clean.capitalize())
        return ("#" + "".join(res))[:100]


