class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        list_dict = sorted(Counter(s).items(), key= lambda x :-x[1])

        for  key,val in list_dict:
            for i in range(val):
                ans.append(key)
        return "".join(ans)
        
        