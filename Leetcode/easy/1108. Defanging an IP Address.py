# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Time: O(n), n = len(address)
        # Space, excluding output: O(1)
        return address.replace(".", "[.]")


