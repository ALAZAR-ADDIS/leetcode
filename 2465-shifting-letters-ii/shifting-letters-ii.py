class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        move=[0]*(len(s)+1)

        for shift in shifts:
            if shift[-1]==0:
                move[shift[0]]+=-1
                move[shift[1]+1]+=1
            else:
                move[shift[0]]+=1
                move[shift[1]+1]+=-1
        for  i in range(1,len(move)):
            move[i]+=move[i-1]
        print(move)
        newChar=""
      


        for i in range(len(s)):
          
            index=((ord(s[i])+move[i])-ord("a"))%26
            
            if index>=0:
                newChar+=chr(ord("a")+index)
            else:
                newChar+=chr(ord("z")+index+1)
           
        return newChar
            
       
       
        