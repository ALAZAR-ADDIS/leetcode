class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        index=[]

        for i in range(len(s1)):
            
            if s1[i] != s2[i] :
                index.append(i)
            if len(index)==2:
                break

        if not len(index) :
            return True
            
        elif len(index)==2:
            s2=list(s2)
            s2[index[0]] , s2[index[1]] = s2[index[1]],   s2[index[0]] 

            return "".join(s2)==s1
        
        return False
        