class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        occ = defaultdict(int)
        
        for i in arr:
            mo =  k - (i % k)
            if  mo in occ:
                occ[mo] -= 1
                if not occ[mo]:
                    occ.pop(mo)
                continue
            elif mo == k and 0 in occ:
                occ[0] -= 1
                if not occ[0]:
                    occ.pop(0)
                continue
            
            occ[i % k] += 1
        print(occ)
        return not len(occ)
            
        
        