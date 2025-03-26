class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def solve(op , cl,path):
            if op == n  and cl == n :
                ans.append("".join(path))
                return 
            
            if op < n:
                path.append("(")
                solve(op + 1, cl ,path)
                path.pop()
            
            
            if op > cl:
                path.append(")")
                solve(op, cl + 1,path)
                path.pop()

        ans = []
        solve(0,0,[])
        return ans
        