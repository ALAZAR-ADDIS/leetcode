class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        l,r=len(a)-1,len(b)-1
        ans=""
        while l>=0 or r>=0:
            if  l>=0 and r>=0:
                temp=int(a[l])+int(b[r])+carry
            elif l>=0:
                temp=int(a[l])+carry
            else:
                temp=int(b[r])+carry
            l-=1
            r-=1

            if temp==2:
                ans+="0"
                carry=1
            elif temp==3:
                ans+="1"
                carry=1
            else:
                ans+=str(temp)
                carry=0
        return ans[::-1] if carry==0 else  "1"+ans[::-1]




            
        