class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(s , t):
            for char in s :
                if s[char] < t[char]:
                    return False
            return True

        count_s= defaultdict(int)
        count_t = defaultdict(int)

        ans =[0,0]
        l =0
        min_size = float("inf")

        freq_s = 0
        freq_t =len(t)

        for char in t:
            count_t[char] += 1
      

        for r in range(len(s)):

            if s[r] in count_t:                
                count_s[s[r]] += 1
                freq_s += 1
           
            while len(count_s)== len(count_t) and check(count_s,count_t) :             

                if s[l] in count_t:
                    count_s[s[l]] -= 1 
                    freq_s -= 1

                    if count_s[s[l]] == 0:
                        count_s.pop(s[l])

                if min_size > r - l + 1:
                    min_size = r - l + 1
                    ans[0] = l
                    ans[1] = r + 1
                
                l+=1 
        left,right = ans
        return s[left:right]
        