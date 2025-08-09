class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # def solve(i,arr):
        #     if i == n:
        #         ans.append("".join(map(str,arr[::])))
        #         return
            
        #     for j in range(i,n):
        #         arr[i],arr[j] = arr[j] , arr[i]
        #         solve(i + 1, arr)
        #         arr[i],arr[j] = arr[j] , arr[i]
        
        # arr = [i +1 for i in range(n)]
        # ans = []
        # solve(0,arr)
        # ans.sort()
        # return ans[k - 1]

        fact = 1
        nums = []
        for i in range(1,n):
            fact *= (i)
            nums.append(str(i))
        nums.append(str(n))
        ans = ""
        k = k- 1
        while True:
           
            ans += nums[ k // fact]
            nums.remove(nums[k//fact])

            if not len(nums):
                break

            k = k % fact
            fact = fact // (len(nums))
        return ans
            


        