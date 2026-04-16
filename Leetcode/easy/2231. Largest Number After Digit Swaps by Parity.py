# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/

class Solution:
    def largestInteger(self, num: int) -> int:
        # Time: O(d log d), d = number of digits in nums
        # Aux space: O(d)
        even = sorted([e for e in str(num) if int(e) % 2 == 0], reverse=True)
        odd = sorted([o for o in str(num) if int(o) % 2 != 0], reverse=True)
        out = []
        i = j = 0
        for n in str(num):
            if int(n) % 2 == 0:
                out.append(even[i])
                i += 1
            else:
                out.append(odd[j])
                j += 1
        return int("".join(out))


