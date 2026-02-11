# Time to write all of below including tests, explanation and time and aux
# and total space: 45 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        temp = []
        letters = []
        k = 0
        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == "[":
                temp.append((letters, k))
                letters = []
                k = 0
            elif ch == "]":
                prev, multiplier = temp.pop()
                letters = prev + letters * multiplier
            else:
                letters.append(ch)
        return "".join(letters)

if __name__ == "__main__":
    sol = Solution()
    assert sol.decodeString("a") == "a"
    assert sol.decodeString("ab") == "ab"
    assert sol.decodeString("2[a]") == "aa"
    assert sol.decodeString("3[a2[ab]]cd") == "aababaababaababcd"

# Explanation: the code iterates through s, and builds the list 'letters' as 
# it goes along by storing intermediary letters and multipliers in temp
# Time: O(n), n = len(s)
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 45 mins):
#   - My complexity comments can be improved, my rewrite is below:
#
# Time: O(n + L), n = len(s), L = length of output string
# Aux space, excluding output and input: O(m), m = max size reached by temp
# Total space, including output, excluding input: O(m + L)
#
#   - Additionally, my tests could have been improved. My rewrite is below:
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.decodeString("a") == "a"
#     assert sol.decodeString("ab") == "ab"
#     assert sol.decodeString("2[a]") == "aa"
#     assert sol.decodeString("3[a2[ab]]cd") == "aababaababaababcd"
#     assert sol.decodeString("10[b]") == "bbbbbbbbbb"
    



