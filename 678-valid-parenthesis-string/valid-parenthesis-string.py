class Solution:
    def checkValidString(self, s: str) -> bool:
 
        # ast = 0
        # stack = []
        # for i in range(len(s)):

        #     if s[i] == ")":
        #         isFound = False
        #         while stack :
        #             poped = stack.pop()
        #             if poped == "(":
        #                 isFound = True
        #                 break
        #             else:
        #                 ast += 1

        #         if not isFound:
        #             if ast:
        #                  ast -= 1

        #             else:                     
        #                 return False
                
        #     else:
        #         stack.append(s[i])
    
   
                
        # while stack:
        #     poped = stack.pop()

        #     if poped == "*":
        #         ast += 1
        #     else:
        #         if ast:
        #             ast -= 1
        #         else:
                 
        #             return False
        # return True
        
        # ast =  0
        # count = 0

        # for i in range(len(s)):
        #     if s[i] == "(":
        #         count += 1
        #     elif s[i] == ")":
        #         count -= 1
        #     else:
        #         ast += 1
            
        #     if count < 0 and abs(count) > ast:
        #         return False
        #     else:
        #         ast -= abs(count)



        minn = 0
        maxx = 0

        for i in range(len(s)):

            if s[i] == "(":
                minn += 1 
                maxx += 1
            elif s[i] == ")":
                minn -= 1 if minn else 0
                maxx -= 1

                if maxx < 0:
                    return False
            else:
                minn -= 1 if minn else 0
                maxx += 1
        return minn <= 0 <= maxx
                
    

                
