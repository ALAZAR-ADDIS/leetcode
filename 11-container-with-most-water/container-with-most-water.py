class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r= len(height) - 1
        max_cap = -float("inf")

        while  l < r:
            max_cap =max(max_cap, min(height[l],height[r]) * (r - l))

            if height[l] < height[r]:
                l+= 1
            else:
                r -= 1
        return max_cap
             
        