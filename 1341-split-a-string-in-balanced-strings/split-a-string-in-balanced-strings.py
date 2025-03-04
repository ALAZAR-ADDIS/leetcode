class Solution:
    def balancedStringSplit(self, s: str) -> int:
        maxx = 0
        dict_= defaultdict(int)

        for i in range(len(s)): 
            if   s[i] == "L" :
                dict_["L"] += 1
            else:
                dict_["R"] += 1           

            if  dict_["L"] == dict_["R"] :
                maxx += 1
                dict_["L"] = 0
                dict_["R"] = 0
          
           

        return maxx
                
        