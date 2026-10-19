class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        i = 0
        j = len(height)-1

        while i < j:
            h1 = height[i]
            h2 = height[j]
            area = max(area, (min(h1,h2) * (j-i)) )

            if h1 > h2:
                j -= 1
            else:
                i += 1

        return area