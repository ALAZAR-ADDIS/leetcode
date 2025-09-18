class Solution:
    def findLucky(self, arr: List[int]) -> int:
        coun = defaultdict(int)
        ans = -1
        prev = -float("inf")
        for i in arr:
            coun[i] += 1
            
        for i in coun:
            if coun[i] == i and prev < i :
                ans = i
                prev = i
        
        return ans
                
        