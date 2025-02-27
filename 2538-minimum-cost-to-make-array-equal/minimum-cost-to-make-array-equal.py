class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        pair = []
        pre = [0]*(len(nums) + 1)
        preC = [0] *(len(nums) + 1)
        ans = float("inf")
        for i in range(len(nums)):
            pair.append([nums[i],cost[i]])
        
        pair.sort(key = lambda x: x[0])

        for i in range(1,len(pre)):
            pre[i] += pre[i - 1] + pair[i -1][0] * pair[i -1][1]
        
        for i in range(1,len(preC)):
            preC[i] += preC[i -1] + pair[i-1][1]
        
        
        for i in range(1,len(preC)):
            print(pair[i-1][0] , preC[-1] , preC[i-1])
            post = (pre[-1]-pre[i - 1]) - ((pair[i-1][0]*(preC[-1] - preC[i-1])))
            prev = (preC[i - 1] * pair[i - 1][0]) -( pre[i - 1])

            print(post,prev)

           
            ans = min(ans,abs(prev) + abs(post))
        return ans

        
        

        
        

        