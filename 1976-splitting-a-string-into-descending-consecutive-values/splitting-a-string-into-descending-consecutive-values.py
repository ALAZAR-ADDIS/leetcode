class Solution:
    def splitString(self, s: str) -> bool:

        def helper(path,i):
            
            if i == len(s):
                if len(path) >=2:
                    return True
                return False

            val = 0
            for i in range(i,len(s)):
                
                val = val * 10 + int(s[i])
                

                if path and path[-1] - val < 1:
                    return False

                if path and path[-1] - val > 1:
                        continue
               
                
                path.append(val)
                check =  helper(path,i + 1)
                if check : return True
                path.pop()
            return False
        return  helper([],0)
                
                


        
          


        