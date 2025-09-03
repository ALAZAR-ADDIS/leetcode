class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr = chars[0]
        count = 0
        temp = []
        for i in range(0,len(chars)):
            if chars[i] == ptr:
                count += 1
                
            else:
                temp.append(ptr)
                if count > 1:
                    temp.extend(list(str(count)))
                ptr = chars[i]
                count = 1
            
            if i == len(chars) - 1 :
                    temp.append(ptr)
                    if count > 1:
                        temp.extend(list(str(count)))
        print(temp)
        for i in range(len(temp)):
            chars[i] = temp[i]

        return len(temp)


        