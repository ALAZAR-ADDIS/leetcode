class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = defaultdict(int)
        count_s = defaultdict(int)
        ans = []
        l = 0
        for char in p:
            count_p[char]+=1
        
        for r in range(len(s)):
            count_s[s[r]] += 1

            while (r - l + 1) > len(p):
                count_s[s[l]]-=1
                if  count_s[s[l]] == 0:
                    count_s.pop(s[l])
                l+=1
            
            if count_s == count_p:
                ans.append(l)
        return ans
        