class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        def helper(n,word):
            if len(word) == n :
                stack.append("".join(word))
                return
         
            if word[-1] == "a":

                word.append("b")
                helper(n,word)

               
                word.pop() 
                word.append("c")  
           

                helper(n,word)

                

            elif word[-1] == "b":

                word.append("a")
                helper(n,word)

                word.pop() 
                word.append("c")

                helper(n,word)
            else:
                word.append("a")
                helper(n,word)

                word.pop() 
                word.append("b")

                helper(n,word)
            word.pop()

        stack = []
        helper(n,["a"])
        helper(n,["b"])
        helper(n,["c"])
       
        return "" if k > len(stack) else stack[k-1]


                
        