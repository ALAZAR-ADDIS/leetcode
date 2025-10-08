class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def solve(n,m):
            if m ==0:
                return n
            
            if n > m:
                rem = n % m 
                return solve(m,rem)
            else:
                rem = m % n
                return solve(n, rem)
        return solve(max(nums), min(nums))