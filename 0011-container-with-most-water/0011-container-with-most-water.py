class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxcont=0
        left,right=0,len(height)-1
        while left<right:
            max=min(height[left],height[right])*(right-left)
            if max>maxcont:
                maxcont=max
            if height[left]>height[right]:
                right-=1
            else :
                left+=1
        return maxcont
