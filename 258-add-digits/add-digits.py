class Solution:
    def addDigits(self, num: int) -> int:
        newNum=num
        total=0
        while num>=10:
            rem=newNum%10
            total+=rem
            newNum=newNum//10
            if newNum==0:
                num=total
                total=0
                newNum=num

        return num

        