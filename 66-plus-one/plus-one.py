class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[len(digits)-1]!=9:
        #     digits[len(digits)-1]+=1
        #     return digits
        # else:
        #     for i in range(len(digits)):
        #         if digits[len(digits)-1-i]==9:
        #             if len(digits)==1:
        #                 digits[0]=1
        #                 digits.append(0)
        #                 return digits
        #             digits[len(digits)-1-i]=0
        #             if digits[0]==0:
        #                 digits.insert(0,1)
        #                 return digits
        #             else:
        #                 if digits[len(digits)-2-i]!=9:
        #                     digits[len(digits)-2-i]+=1
        #                     return digits

        carry=1
        r=len(digits)-1
        while r>-1 and carry:
            carry=0
            total=digits[r]+1+carry
            carry=total//10
            rem=total%10
            digits[r]=rem
            r-=1
        if carry:
            digits.insert(0,carry)
        return digits

