class Solution:
    def frequencySort(self, s: str) -> str:
        #cout cort algorithm
        freqList=[[] for i in range(len(s)+1)]
        wordList={}
        for word in s:
            wordList[word]=1+wordList.get(word,0)
        
        for word,freq in wordList.items():
            freqList[freq].append(word)
        resultString=""

        for i in range(len(freqList)-1,0,-1):
            for j in freqList[i]:
                    resultString+=(j*i)
                    
        return resultString

         
        