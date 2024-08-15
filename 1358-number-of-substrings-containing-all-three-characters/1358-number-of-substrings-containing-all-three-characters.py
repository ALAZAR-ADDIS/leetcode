class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #create a  hash map(dictinary)
        #left pointer
        #right pointer
        #counter
        # every  element pointed by  r pointer will be added to my dictionary
        #if all three exists in the dictionary i will shift the left pointer and check and increase my count/ remove my element from dict

        letter={}
        counter=0
        l=0
        for r in range(len(s)):
            letter[s[r]]=1+letter.get(s[r],0)
            while len(letter)==3:
                letter[s[l]]=letter[s[l]]-1
                if letter[s[l]]==0:
                    letter.pop(s[l]) 
                l+=1
                counter+=len(s)-r
        return counter