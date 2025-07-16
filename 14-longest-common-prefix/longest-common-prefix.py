class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #find the shortes string  from the list
        leng = len(strs[0])
        sChar = strs[0]
        for  i in range(len(strs)):
            if leng > len(strs[i]):
                leng = len(strs[i])
                sChar = strs[i]
        common = ""

        #iterate for every char in that short string
        for index, char in enumerate(sChar):
             
            for word in strs:
                if char != word[index] :  #if not return that common string that we find lately
                    return common 
            common += char #if it is commone add to the answer
        
        return common

           
           
        