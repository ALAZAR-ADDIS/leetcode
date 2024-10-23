class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
      #iterate 0-ilen-1
        for i,n in  enumerate(s):
            index=ord(n)-ord("a")
            dis=distance[index]+1
            print(i +dis <len(s) and n==s[i+dis],i-dis>=0 and  i==s[i-dis])
            

            if  (i +dis <len(s) and n==s[i+dis]) :
                continue
            elif (i-dis>=0 and  n==s[i-dis]):
                continue
            else :return False
        return True
    
                