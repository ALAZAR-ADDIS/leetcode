class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict={}
        ans=[]
        for i in cpdomains:
            freq,dirc=i.split(" ")
            freq=int(freq)
            cpd=dirc.split(".")
            for j in range(len(cpd)-1,-1,-1):
                val=".".join(cpd[j:])
                dict[val]=dict.get(val,0)+freq
        print(dict)
        for key,val in dict.items():
            ans.append(f"{val} {key}")
        return ans


                