class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
      
            if tokens[i] == "+":
               
                val = stack.pop() + stack[-1]
                stack[-1] = val
            elif tokens[i] == "-":
                poped = stack.pop()
                val = stack[-1] - poped
                stack[-1] = val
            elif tokens[i] == "*":
                val = stack.pop() * stack[-1]
                stack[-1] = val
            elif tokens[i] == "/":
                poped = stack.pop()
                val =  int(stack[-1]/poped)
                stack[-1] = val
            else:
                stack.append(int(tokens[i]))  
        return stack[-1]