class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=s.strip().split(" ")
        return len(arr[len(arr)-1])

        