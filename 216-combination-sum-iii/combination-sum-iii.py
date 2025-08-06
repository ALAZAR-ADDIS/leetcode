class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i + 1 for i in range(9)]

        def solve(i, total,path):
            if i == 9 or  total >= n:
                if total == n and len(path) == k:
                    ans.append(path[::])
                return 
            
            path.append(nums[i])
            total += nums[i]
            solve(i + 1,total,path)

            path.pop()
            total -= nums[i]
            solve(i + 1,total,path)
        ans = []
        solve(0,0,[])
        return ans
        