class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word=[i for i in word]
        index=0
        stack=[]
        for i in range(len(word)):
            if  stack and word[i]==ch :
                stack.append(word[i])
                while stack:
                    word[index]=stack.pop()
                    index+=1
                return "".join(word)
            else:
                if not stack and word[i]==ch:
                    return "".join(word)
                stack.append(word[i])
                
        return "".join(word)
                


        