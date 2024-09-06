class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        list1=["" for i in range(len(s))]
        for i in range(len(indices)):
          list1[indices[i]]=s[i]

        return "".join(list1)