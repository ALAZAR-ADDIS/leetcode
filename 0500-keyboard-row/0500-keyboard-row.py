class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        rowstore=[]
        wordstore=[]
        for word in words:
            for letter in word:
                if letter.lower() in row1:
                    rowstore.append(1)
                elif letter.lower() in row2:
                    rowstore.append(2)
                elif letter.lower() in row3:
                    rowstore.append(3)
            for k in rowstore:
                if k!=rowstore[0]:
                    wordstore.append(word)
                    break
            rowstore.clear()
        for i in wordstore:
            words.remove(i)
        return words