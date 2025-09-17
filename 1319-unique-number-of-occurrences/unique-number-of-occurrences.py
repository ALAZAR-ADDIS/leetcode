class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counte = Counter(arr)
        const = counte[arr[0]]
        occ =  set()
        for k in counte:
            if counte[k] in occ:  
                return False
            occ.add(counte[k])
        
        return True