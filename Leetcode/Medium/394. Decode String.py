# Time to write all of below including tests, explanation and time and aux
# and total space: 34 mins

# Problem: https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        out = []
        temp = []
        k = 0
        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == "[":
                temp.append((out, k))
                out = []
                k = 0
            elif ch == "]":
                prev, multiplier = temp.pop()
                out = prev + multiplier * out
                k = 0
            else:
                out.append(ch)
        return("".join(out))

if __name__ == "__main__":
    sol = Solution()
    assert sol.decodeString("a") == "a"
    assert sol.decodeString("ab") == "ab"
    assert sol.decodeString("2[a]") == "aa"
    assert sol.decodeString("3[a2[ab]]cd") == "aababaababaababcd"
    assert sol.decodeString("10[b]") == "bbbbbbbbbb"

# Explanation: the code iterates through s, and builds the list 'out' as 
# it goes along by storing intermediary letters and multipliers in temp
# Time: O(n + L), n = len(s), L = len(out)
# Space: excluding output: O(d + L), d = max nesting depth
  

