

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # Time: O(n log n), n = len(score)
        # Space: O(n)
        out = [""] * len(score)
        ranks = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        place = 1
        for s, i in ranks:
            if place == 1:
                out[i] = "Gold Medal"
            elif place == 2:
                out[i] = "Silver Medal"
            elif place == 3:
                out[i] = "Bronze Medal"
            else:
                out[i] = str(place)
            place += 1
        return out


