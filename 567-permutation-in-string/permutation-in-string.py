class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = defaultdict(int)
        dict_s2 = defaultdict(int)
        l = 0

        for i in range(len(s1)):
            dict_s1[s1[i]] += 1 

        for r in range(len(s2)):
            dict_s2[s2[r]] += 1

            while r - l + 1 > len(s1):

                dict_s2[s2[l]]  -= 1

                if dict_s2[s2[l]] == 0:

                    dict_s2.pop(s2[l])
                l += 1
   
            if dict_s1 == dict_s2:
                return True
        return False

        
        
        
        