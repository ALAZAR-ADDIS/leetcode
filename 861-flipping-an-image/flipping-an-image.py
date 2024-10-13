class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            l,r=0,len(i)-1
            while l<=r:
                i[r],i[l]=i[l],i[r]
                if l!=r:
                    i[l]=0 if i[l]==1 else 1
                    i[r]=0 if i[r]==1 else 1
                else:
                    i[l]=0 if i[l]==1 else 1
            
                l+=1
                r-=1
        return image
        