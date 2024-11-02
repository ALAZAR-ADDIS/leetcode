class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        ans=[]
        for path in paths:
            root,*files=path.split(" ")
            

            for file in files:
                f,content=file.split("(")
                newRoot=root+"/"+f
               
                dict[content].append(newRoot)
        for val in dict.values():
            if len(val)>1:
               ans.append(val)
        return ans


        

        