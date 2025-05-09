class quickUnion:
    def __init__(self,par):
        self.parent = [i for i in range(len(par) + 1)]
        self.rank = {i:0 for i in range(len(par) + 1)}


    def find(self,x):
        if x == self.parent[x]:
            return x
        
        root = self.find(self.parent[x])
        self.parent[x] = root
        return root
    
    def union(self,x,y):
        par = self.find(x)
        par2  = self.find(y)
        if par == par2:
            return  False

        
        if self.rank[par] == self.rank[par2]:
            self.parent[par] = par2
            self.rank[par2] += 1        
        elif self.rank[par] > self.rank[par2]:
            self.parent[par2] = par
        else:
            self.parent[par] = par2

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        emailPair = defaultdict(int)
        uf = quickUnion(accounts)

        for index, email in enumerate(accounts):
            for e in email[1:]:
                if e not in emailPair:
                    emailPair[e] = index
                else:
                    uf.union(index,emailPair[e])
        joined = defaultdict(list)
        
        for email, index in emailPair.items():
            i = uf.find(index)
            joined[i].append(email)
        
        answer = []

        for index, emails in joined.items():
            answer.append([accounts[index][0]] + sorted(emails))
        
        return answer



       