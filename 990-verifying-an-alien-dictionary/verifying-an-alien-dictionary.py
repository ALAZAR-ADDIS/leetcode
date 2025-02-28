class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        i = 0
        order_s = defaultdict(int)

        for char in order:
            order_s[char] = i
            i += 1

        for i in range(len(words) - 1):            

            for j in range(len(words[i])):

                if  j >= len(words[i + 1]) or order_s[words[i][j]] > order_s[words[i + 1][j]]:
                    return False
                elif order_s[words[i][j]] < order_s[words[i + 1][j]]:
                    break

               
        return True

        