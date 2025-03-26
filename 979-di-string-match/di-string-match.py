class Solution:
    def diStringMatch(self, s: str) -> List[int]:

        ans = []
        stack = []

        for i in range(len(s) + 1): 
                       
            stack.append(i)
            while stack and (i == len(s) or s[i] =="I"):
                ans.append(stack.pop())

        return ans

        