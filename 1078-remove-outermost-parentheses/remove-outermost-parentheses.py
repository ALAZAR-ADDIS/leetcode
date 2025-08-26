class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = defaultdict(int)
        ans = []
        stack = []

        for i in s:
            count[i] += 1
            if count["("] == count[")"]:
                
                if stack :
                    for i in range(1,len(stack)):
                        ans.append(stack[i])
                stack.clear()
                   
                
                    
            else:
                stack.append(i)
        
        return "".join(ans)
        