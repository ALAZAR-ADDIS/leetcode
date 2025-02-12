class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        curr_char = set()
        last_index = {}
        ans = []
        l=0
        for index,char in enumerate(s):
            last_index[char] = index
        
        for index,char  in enumerate(s):
            curr_char.add(char)

            if index == last_index[char]:
                curr_char.remove(char)
            
            if not len(curr_char) :
                ans.append(index - l +1)
                l = index + 1
        return ans
                
        
        