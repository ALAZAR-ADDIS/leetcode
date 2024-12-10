class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        #count a window of 3 befor begining the process so that you could use  static sliding window technic
        #then move tha window until the left point to the end of the list
        #inorder to move to the back of the list again use the modulus opertion
        # for every left move if the consucetive values of  the list are  alternating decrease the value of the a
        
        alt=0
        for r in range(2):
            if colors[r]!=colors[r+1]:
                alt+=1
        
        ans= 1 if alt==2 else 0
        
        l=0
        r=2
        while l<len(colors)-1:
            if colors[l]!=colors[l+1]:
                alt-=1
                
            if colors[r%len(colors)]!=colors[(r+1)%len(colors)]:
                alt+=1
            ans+=1 if alt==2 else 0
               
            


            r+=1
            l+=1
        return ans

        