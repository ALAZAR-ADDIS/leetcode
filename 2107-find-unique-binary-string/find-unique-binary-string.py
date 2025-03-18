class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        

        def solve(n,nums,val = ""):
            if len(val) > n:
                return 

            if len(val) == n and val not in nums:
                return  val
            
            val1 = solve(n,nums,val= val + "0")
            val2 = solve(n,nums,val= val +"1")

            if val1:
                return val1
            if val2:
                return val2
        return solve(len(nums),set(nums),"")

        