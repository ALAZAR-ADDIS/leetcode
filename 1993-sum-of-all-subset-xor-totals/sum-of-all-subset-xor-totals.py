class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []
        anss = 0
        def solve(i,path):
            if i == len(nums):
                ans.append(path[::])
                return 
            

            path.append(nums[i])
            solve(i + 1,path)
            path.pop()
            solve(i + 1,path)
        solve(0,[])
        for vals in ans:
            cur = 0
            for i in vals:
                cur ^= i
            anss += cur

        return anss

            