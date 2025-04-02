class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(summ ,path,j):
            if j == len(candidates) or summ >= target:
                temp = []
                if summ == target:
                    print(path,j)
                    temp.append(path[::])               

                return temp

            path.append(candidates[j])
            summ += candidates[j]

            pick = helper(summ,path,j)

            path.pop()
            summ -= candidates[j]

            noPick = helper(summ,path,j+ 1)

            pick.extend(noPick)

            return pick


         
           
        return helper(0,[],0)

                
            
                    
        