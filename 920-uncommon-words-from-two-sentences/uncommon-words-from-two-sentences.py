class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        total = []
        total.extend(s1.split())
        total.extend(s2.split())
        s1 = s1.split()
        s2 = s2.split()
        cs = Counter(s1)
        cs2 = Counter(s2)
        ans = []
        for i in set(total):
            if i in s1 and i in s2:
                continue
            if cs[i] == 1 or cs2[i] == 1:
                ans.append(i)
        
        return ans
            
        