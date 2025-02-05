class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        count_word = Counter(chars)
    
        ans=0

        for word in words:
            all_occ=True

            count_word_list=Counter(word)

            for i in count_word_list:

                if  count_word[i] <  count_word_list[i] :
                  
                    all_occ=False
                    break
            ans += len(word) if all_occ else 0
        return ans
    
            

        