class Solution:
    def totalNQueens(self, n: int) -> int:


        def solve(col,path):
                
                if col == n:                    
                    if len(path) == n:
                        return 1
                    return  0
                
                res = 0           
                pos = ["."] * n
                
                for i in range(n):
                    if i in cols  or  i + col in pv  or i - col in nv:
                        continue

                    pv.add(i + col)
                    nv.add(i - col)
                    cols.add(i)

                    pos[i] = "Q"
                    path.append("".join(pos[::])) 
                    res += solve(col + 1, path)
                    
                    pos[i] = "."
                    path.pop()

                    pv.remove(i + col)
                    nv.remove(i - col)
                    cols.remove(i)
                return res            





        pv = set()
        nv= set()
        cols = set()

        return solve(0,[])
        