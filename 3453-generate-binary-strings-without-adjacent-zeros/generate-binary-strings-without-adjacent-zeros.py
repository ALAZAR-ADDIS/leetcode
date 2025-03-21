class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        def solve(ans , i):

            if i==n:               
                vari.append("".join(ans))
                return 

            if not ans or (ans and ans[-1]!="0"):
                ans.append("0")
                solve(ans,i+1)
                ans.pop()
        
           
            
            ans.append("1")
            solve(ans ,i+1)
            ans.pop()

           
           
        vari = []
        solve([],0)
        return vari