class Solution:
    def isValid(self, s: str) -> bool:
        #check if the element in the  list is close or open bracket
        #if open move  add to the stack
        #else check i the stak has and element that can be pop end  is suitable closing bracket if so pop else return false
        stack=[]
        closingBrackets={"}",")","]"}
        Dict={"}":"{","]":"[",")":"("}

        for i in range(len(s)):
            if stack and  s[i] in closingBrackets:
                if   stack[-1]==Dict[s[i]]:
                    stack.pop()
                    continue
                else:
                    return False

            stack.append(s[i])
        return False if len(stack) else True
            

       