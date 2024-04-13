class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        if letters[len(letters)-1]<=target:
            return letters[0]
        while right>=left :
           
            mid=(right+left)//2
            if letters[mid]>target:
                right=mid-1
            else:
                left=mid+1
        if right==len(letters)-1:
            return letters[right]
        else:
            return letters[right+1]
        