class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxWat=-1
        while l<r:
            maxWat=max(maxWat,min(height[l],height[r])*(r-l))
            if height[l]>=height[r]:
                r-=1
            else:
                l+=1
        
        return maxWat
        