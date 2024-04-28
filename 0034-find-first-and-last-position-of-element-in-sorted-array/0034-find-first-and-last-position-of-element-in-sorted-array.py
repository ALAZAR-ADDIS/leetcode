class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        index=[]
        while right>=left :
            mid=(right+left)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1 
        index.append(left)
        
        left=0
        right=len(nums)-1
        isfound=False
        while right>=left :
            mid=(right+left)//2
            if nums[mid]==target:
                isfound=True
            if nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        index.append(right)
        if isfound:
            return index
        return [-1,-1]
                
        