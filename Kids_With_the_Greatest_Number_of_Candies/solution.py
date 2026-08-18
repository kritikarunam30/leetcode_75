class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatest = max(candies)

        for each in candies:
            buffer = each + extraCandies
            if buffer >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result
