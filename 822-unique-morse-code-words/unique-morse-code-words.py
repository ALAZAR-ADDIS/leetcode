class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        sign = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = []
        for word in words:
            temp = ""
            for i in word:
                temp += sign[ord(i) - ord("a")]
            ans.append(temp)
        return len(set(ans))
        
        