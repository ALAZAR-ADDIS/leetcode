class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def solve(i,path):
            if i ==len(s):
                if len(path)== 4:
                    ans.append(".".join(map(str,path)))
                return 
            
            if len(path) == 4:
                return 
            val = 0
            
            for j in range(i,len(s)):



                val = val * 10 + int(s[j])

                if val > 255:
                    return
                
                if s[i] =="0" and val == 0:
                    path.append(val)
                    solve(j + 1,path)
                    path.pop()
                    return 
                path.append(val)
                solve(j + 1,path)
                path.pop()
        ans = []
        solve(0,[])
        return  ans

            




        