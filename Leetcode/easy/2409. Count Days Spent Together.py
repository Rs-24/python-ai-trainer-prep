# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-days-spent-together/description/

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Time: O(1)
        # Space: O(1)
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        a_a = int(arriveAlice[3:]) + sum(m[:int(arriveAlice[:2]) - 1])
        a_l = int(leaveAlice[3:]) + sum(m[:int(leaveAlice[:2]) - 1])
        b_a = int(arriveBob[3:]) + sum(m[:int(arriveBob[:2]) - 1])
        b_l = int(leaveBob[3:]) + sum(m[:int(leaveBob[:2]) - 1])
        return max(0, min(a_l, b_l) - max(a_a, b_a) + 1)


