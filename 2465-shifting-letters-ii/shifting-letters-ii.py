class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0] * (len(s) + 1)
        ans = []

        for start,end,dirc in shifts:
            if dirc == 0 :
                shift[start] -= 1
                shift[end + 1] += 1
            else:
                shift[start] += 1
                shift[end + 1] -= 1
        for i in range(1,len(shift)):
            shift[i] += shift[i - 1]
            
        for i in range(len(s)):
            ascii_val = ((ord(s[i]) -  ord("a")) + shift[i]) % 26 + ord("a")
            ans.append(chr(ascii_val))

        return "".join(ans)
            
        
                
        