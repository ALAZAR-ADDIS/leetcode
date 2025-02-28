class Solution:
    def equalFrequency(self, word: str) -> bool:
        count_word = defaultdict(int)
        count_freq = defaultdict(int)

        for char in word:
            count_word[char] += 1
        
        for freq in count_word.values():
            count_freq[freq] += 1
        
        if len(count_freq) > 2:
            return False
        elif len(count_freq) == 2:
            
         
            key1,key2 = count_freq.keys()
            minKey = min(key1,key2)
            freq = count_freq[max(key1,key2)]

            if abs(key1 - key2) * freq <= 1:
                return True
            elif minKey == 1 and count_freq[minKey] == 1:
                return True
            else:
                return False
        else:
            key = list(count_freq.keys())[0]
        

            if key == 1:
                return True
            else:
                if count_freq[key]== 1:
                    return True
                else:
                    return False
        



        

        