class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = defaultdict(int)
        def dp(i):
            if i >= len(questions):
                return 0
            
            if i in memo:
                return memo[i]
            
            solve = dp(i + questions[i][1] + 1) + questions[i][0]
            notsolve = dp(i + 1)

            memo[i] = max(solve, notsolve)

            return memo[i]

        return dp(0)
        