class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack=[]
        # counter=[]
        # for i in  s:
        #     if  stack and stack[-1]==i:
        #         counter[-1]+=1
        #     else:                
        #         counter.append(1)
        #     stack.append(i)
        #     if counter[-1]==k:
        #         while counter[-1]>0:
        #             counter[-1]-=1
        #             stack.pop()
        #         counter.pop()
        # return "".join(stack)
        stack=[]
        counter=[]
        for i in  s:
            if  stack and stack[-1]==i:
                counter[-1]+=1
            else:                
                counter.append(1)
                stack.append(i)
            if counter[-1]==k:
                stack.pop()
                counter.pop()
        return "".join([stack[i]*counter[i] for i in range(len(stack))])
                
                
            