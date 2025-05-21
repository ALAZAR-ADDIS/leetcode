class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def solve(path,i):
            if i >= len(s):
                ans.append("".join(path[::]))
                return 
            

            if not s[i].isalpha():
                path.append(s[i])                
                solve(path,i + 1)
                path.pop()

            else:
                path.append(s[i].upper())
                solve(path,i + 1)
                path.pop()

                path.append(s[i].lower())
                solve(path, i + 1)
                path.pop()

        ans = []
        solve([],0)
        return ans
                