

from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products: list, searchWord: str) -> list:
        # Time: O(n log n)
        # Space: O(n * len(searchword))
        products.sort()
        ans = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            i = bisect_left(products, prefix)
            temp = []
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    temp.append(products[j])
            ans.append(temp)
        return ans


