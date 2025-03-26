class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # stack , res = [], []

        # for i in range(len(pattern) + 1):
        #     stack.append(i + 1)

        #     while stack and (i== len(pattern) or pattern[i]=="I"):
        #         res.append(str(stack.pop()))
        # return "".join(res)


        def solve(index,path):
          
            if len(path) == len(pattern) + 1: 
                              
                return "".join(map(str,path))
            
            for i in range(1,10):

                if i in maped:
                    continue
              
                if path and ((pattern[index -1]=="I" and path[-1] >= i) or (pattern[index - 1]=="D" and path[-1] <= i)):
                    continue
                
                path.append(i)
                maped.add(i)
                
                val = solve(index + 1,path)
                
                if val:
                    return val
               
                path.pop()
                maped.remove(i)
        maped = set()
        return solve(0,[])


            
       