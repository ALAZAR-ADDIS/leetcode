class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def solve(path, j):
            if j == len(s):
                ans.append(path[::])
                return 
            
            for i in range(j,len(s)):
                temp = s[j:i + 1:]
              
                if temp == temp[::-1]:
                    path.append(s[j : i + 1])
                    solve(path, i + 1)
                    path.pop()
        
        ans = []
        solve([],0)
        return ans
        