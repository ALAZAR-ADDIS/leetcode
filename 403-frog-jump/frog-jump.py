class Solution:
    def canCross(self, stones: List[int]) -> bool:
      

        def dp(i,prev,k):
            if i == len(stones) - 1 :
                # print(i,prev,k)
                             
                return stones[prev] + k == stones[i]
            
            pos = (i,prev, k)
            if pos in memo:
                return memo[pos]

            state = False
            if stones[prev] + k == stones[i]:
                print(i,prev,k,"done")
                if k - 1 > 0:
                    state = state or dp(i + 1, i, k - 1)
                state = state or dp(i + 1,i,k + 1) or dp(i + 1,i,k ) 
            elif stones[prev] + k < stones[i]:
                state = False
            else:                
                state = state or dp(i + 1,prev,k)

            memo[pos] = state
            return memo[pos]
        memo = defaultdict(bool)
        return  dp(1,0,1)

            
            
        