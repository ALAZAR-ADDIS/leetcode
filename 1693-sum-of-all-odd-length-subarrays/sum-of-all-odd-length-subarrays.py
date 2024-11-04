import math
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # total = 0

        # for num in arr:
        #     total += num

        # i = 0
        # j = 1

        # while i < j < len(arr):
        #     if (j - i + 1) % 2 != 0:
        #         total += sum(arr[i: j + 1])
        #         j += 1
        #     else:
        #         j += 1

        #     if j == len(arr):
        #         i += 1
        #         j = i + 1

        # return total
        
        l=len(arr)
        total=0
        for i in range(len(arr)):
            count=math.ceil(((i+1) *(l-i))/2.0)
            total+=count*arr[i]
        return total
            

        