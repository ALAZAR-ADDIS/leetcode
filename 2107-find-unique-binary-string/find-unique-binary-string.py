class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        

        # def solve(n,nums,val = ""):
        #     if len(val) > n:
        #         return 

        #     if len(val) == n and val not in nums:
        #         return  val
            
        #     val1 = solve(n,nums,val= val + "0")
        #     val2 = solve(n,nums,val= val +"1")

        #     if val1:
        #         return val1
        #     if val2:
        #         return val2
        # return solve(len(nums),set(nums),"")

        def solve(i,arr):
            if i == len(arr):
                return None if "".join(arr) in numSet else  "".join(arr)
            
            val = solve(i + 1,arr)
            if val:
                return val

            arr[i] = "1"
            val2 = solve(i + 1, arr)
            
            if val2 :
                return val2


        numSet = set(nums)
        arr = ["0"] * len(nums)
        return solve(0,arr)

        