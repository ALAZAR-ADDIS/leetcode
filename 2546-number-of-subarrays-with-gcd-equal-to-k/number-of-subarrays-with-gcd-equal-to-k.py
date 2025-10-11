class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        def GCF(n,m):
            if m ==0:
                return n
            
            return GCF(m, n % m)

        
        ans = 0
        for l in range( len(nums)):
            gcd = nums[l]
            for j in range(l, len(nums)):
                gcd = GCF(nums[j],gcd)

                if gcd == k:
                    ans += 1
                
                
        return ans

        return ans
            
        