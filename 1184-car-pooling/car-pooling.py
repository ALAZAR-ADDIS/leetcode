class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums =  [0]* 1002
        for pp,star,end in trips:
            nums[star] += pp
            nums[end ] += -pp
        
        for i in range(1,len(nums)):
            nums[i] += nums[i- 1]

            if nums[i] > capacity:
                return False

        for i in range(len(nums)):          

                if nums[i] > capacity:
                    return False
        return True
        