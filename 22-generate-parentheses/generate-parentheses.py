class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #if open=close=n return all the parantasis
        #if open>close add closing paranthasis paranthasis
        #if  opening is <n app opening paranthasis
        ans,stack=[],[]

        def backTrack(openB,closeB):
            if openB==closeB==n:
                ans.append("".join(stack))
                return 
            
            if openB<n:
                stack.append("(")
                backTrack(openB+1,closeB)
                stack.pop()
            if openB>closeB:
                stack.append(")")
                backTrack(openB,closeB+1)
                stack.pop()
        backTrack(0,0)
        return ans
        
        