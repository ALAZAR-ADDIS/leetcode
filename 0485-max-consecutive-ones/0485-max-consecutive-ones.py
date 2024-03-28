class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        list1=[]
        for num in nums:
            if num==1:
                count+=1
            else:
                list1.append(count)
                count=0
        list1.append(count)
        return max(list1)

            