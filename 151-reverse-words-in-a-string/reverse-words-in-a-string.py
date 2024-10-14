class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        new=""

        # word=word[::-1]
        
       
        # return " ".join(word)
        while word:
            new+=word.pop()
            if word:
                new+=" "
        return new
            



        