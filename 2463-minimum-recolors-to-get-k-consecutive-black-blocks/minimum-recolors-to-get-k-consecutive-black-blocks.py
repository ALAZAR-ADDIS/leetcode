class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #minReplace is thre minimum number of characrers to be replaced
        #create a k sized dictionary to begin wiht the static windw size
        # theck the number if whites as the mimumum  the replaced to begin the process
        #add one from the front  add the white or blak freq on the dict 
        #decreast  the freq while moving from the left
        
        count={}
        for i in range(k):
            count[blocks[i]]=count.get(blocks[i],0)+1
        minReplac=count.get("W",0)
        l=0
        for r in range(k,len(blocks)):
            count[blocks[l]]-=1
            count[blocks[r]]=count.get(blocks[r],0)+1
            minReplac=min(minReplac,count.get("W",0))
            l+=1
        return minReplac


        