class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(n):
            if n == len(cost) - 1:
                return cost[n]
            
            if n == len(cost) :
                return 0
            
            if n in memo:
                return memo[n]
            
            cost1 = dp(n +  1)
            cost2 = dp(n + 2)
            memo[n] = min(cost1 , cost2) + cost[n]

            return memo[n]
        memo = defaultdict(int)
        return min (dp(1), dp(0))
        