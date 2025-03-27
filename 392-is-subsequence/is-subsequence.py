class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # def solve(path , i):
        

        #     if i == len(t):
        #         if "".join(path) == s:
        #             return True
        #         return False        

        #     if len(path) > len(s):
        #         return False

        #     path.append(t[i])
        #     val = solve(path, i + 1)
        #     if val : return True
            

        #     path.pop()
        #     val = solve(path, i + 1)
        #     if val :
        #         return True
        #     return False

            
        # return  solve([],0)

        ptr = 0
        for i in range(len(t)):
            if ptr < len(s) and  s[ptr] == t[i]:
                ptr += 1
        return ptr == len(s)
    

        
            

        