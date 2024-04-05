class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        rightpointer=len(nums)-1
        leftpointer=0
        flag=0
        while leftpointer<rightpointer:
            product=rightpointer*leftpointer
            if nums[rightpointer]==nums[leftpointer] and (product%k)==0:
                    flag+=1
            rightpointer-=1
            if rightpointer==leftpointer:
                leftpointer+=1
                rightpointer=len(nums)-1
        return flag