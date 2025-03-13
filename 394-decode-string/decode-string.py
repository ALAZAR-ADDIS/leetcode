class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):

          
            if s[i] == "]":
                char = []

                while stack and stack[-1].isalpha():
                    char.append(stack.pop())

                if stack[-1] == "[":
                    stack.pop()

                char = "".join(char[::-1])
                num = []

                while stack and not(stack[-1].isalpha()):
                    if stack[-1] != '[':
                        num.append(stack.pop())
                    else:
                        stack.pop()
                        break
                num = int("".join(num[::-1])) if num else 1

                stack.append( num * char)
                continue
            stack.append(s[i])
            
                
            


        

        return "".join(stack)
                
            

                    

        
        

            

        