class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_km = max(trip[2] for trip in trips )
        timeline = [0] * (max_km + 1)
        for passengers,start,end in trips :
            timeline[start] += passengers 
            timeline[end] -= passengers 

            passengers_load = list(accumulate(timeline)) 

            for load in passengers_load :
                if load > capacity :
                    return False 
        return True                 


     
