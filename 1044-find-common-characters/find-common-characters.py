class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        short_str =" "* 101
        freq = []
        ans = []
        for word in words:
            if len(word) < len(short_str):
                short_str = word
            freq.append(Counter(word))

        for char in short_str:
            min_freq= freq[0][char]
            for i in range(len(freq)): 
                min_freq = min(min_freq, freq[i][char])
                if freq[i][char] :
                    freq[i][char] -= 1
            if min_freq:
                ans.append(char)

        return ans
                


    





            
        