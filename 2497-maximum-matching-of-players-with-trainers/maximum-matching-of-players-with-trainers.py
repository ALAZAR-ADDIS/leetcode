class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        #first fort both of the arrays
        #second point the pointer from the on the 0th index
        #if players [] >trainers [] trainers+=1 else count and players+=1 trainers+=1
        players.sort()
        trainers.sort()
        i,j=0,0
        ans=0
        while  i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                j+=1
                i+=1
                ans+=1
            
            else:j+=1
        return ans

        