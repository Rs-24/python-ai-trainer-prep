# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/

class Solution:
    def modifyString(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(1)
        out = []
        for i, ch in enumerate(s):
            if ch == "?":
                prev = -1 if not out else out[-1]
                next = -1 if i == len(s) - 1 else s[i + 1]
                for new_ch in ["a", "b", "c"]:
                    if new_ch != prev and new_ch != next:
                        out.append(new_ch)
                        break
            else:
                out.append(ch)
        return "".join(out)


