class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):

          
            if s[i] == "]":
                char = []

                while stack and stack[-1] != "[":
                    char.append(stack.pop())

                stack.pop()

                char = "".join(char[::-1])
                num = []

                while stack and stack[-1].isdigit():
                        num.append(stack.pop())
                num = int("".join(num[::-1])) if num else 1

                stack.append( num * char)
            else:
                stack.append(s[i])
                          
            
        return "".join(stack)
                
            

                    

        
        

            

        