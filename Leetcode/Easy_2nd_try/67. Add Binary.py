# Time to write all of below including tests, why the solution works and time 
# and space complexity: 50 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        diff = len(a) - len(b)        
        if diff > 0:
            b += "0" * diff
        elif diff < 0:
            a += "0" * abs(diff)
        result = []
        carry = 0
        total = 0
        for i in range(len(a)):
            total = int(a[i]) + int(b[i]) + carry
            result.append(str(total % 2))
            carry = total // 2
        if carry == 1:
            result.append("1")
        out = []
        i = len(result) - 1
        while i >= 0:
            out.append(result[i])
            i -= 1
        return "".join(out)

if __name__ == "__main__":
    sol = Solution()
    assert sol.addBinary("0", "0") == "0"
    assert sol.addBinary("0", "1") == "1"
    assert sol.addBinary("1", "0") == "1"
    assert sol.addBinary("1", "1") == "10"
    assert sol.addBinary("1", "11") == "100"
    assert sol.addBinary("1", "100") == "101"
    assert sol.addBinary("11", "11") == "110"
    assert sol.addBinary("101", "011") == "1000"

# Explanation: the code reverses a and b and ensures they are the same length,
# then does binary addition using a carry variable, and stores the result in 
# the list 'result'. Then it reverses this list and stores it in the variable
# out, then joins this variable together to form a string and returns this
# string
# Time: O(M), M = max(len(a), len(b))
# Aux space, excluding output and input: O(n + m), n = len(a), m = len(b)
# Total space, including output, excluding input: O(n + m)

# Learning lessons (done after completing all of above in 50 mins):
#   - No major learning lessons




