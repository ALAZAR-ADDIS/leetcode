class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def solve(path,total,target,i):
            if total >= target or i == len(candidates):
                if total == target:
                    ans.append(path[::])                
                return
          
            
            path.append(candidates[i])
            total += candidates[i]
            solve(path,total,target,i + 1)

            while i < len(candidates)-1 and  candidates[i] == candidates[i + 1]:
                i +=  1            
                     
            path.pop()
            total -= candidates[i]
                
            solve(path,total,target,i + 1)
        
     
        ans = list()
        candidates.sort()
        solve([],0,target,0)
        return ans


