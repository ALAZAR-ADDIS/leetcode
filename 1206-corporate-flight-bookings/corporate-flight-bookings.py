class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        reserSeats=[0]*(n+1)
        for i in bookings:
            reserSeats[i[0]-1]+=i[-1]
            reserSeats[i[1]]-=i[-1]
        for i in range(1,len(reserSeats)):
            reserSeats[i]+=reserSeats[i-1]
        return reserSeats[:-1]
