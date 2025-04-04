class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def solve(col,path):
                
                if col == n:
                    temp =[]
                    if len(path) == n:
                        temp.append(path[::])
                    return  temp
                
                res = []            
                pos = ["."] * n
                
                for i in range(n):
                    if i in cols  or  i + col in pv  or i - col in nv:
                        continue

                    pv.add(i + col)
                    nv.add(i - col)
                    cols.add(i)

                    pos[i] = "Q"
                    path.append("".join(pos[::])) 
                    ans = solve(col + 1, path)
                    res.extend(ans)

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