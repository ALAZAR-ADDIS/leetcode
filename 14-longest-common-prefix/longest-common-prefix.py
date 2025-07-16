class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find the   shortest string from the array

        leng = len(strs[0])
        shortest_wrd = strs[0]

        for i in range(len(strs)):
            if leng >  len(strs[i]):
                shortest_wrd = strs[i]
                leng = len(strs[i])

        #iterate over the  shortest string  and check if that char is common 
            #if not common break and leave and return the  commons 
            #add  the common char to the string
        common = ""
            
        for index,char in enumerate(shortest_wrd):
            for i in range(len(strs)):
                if char != strs[i][index]:
                    return common
            common += char
        return common
            
        