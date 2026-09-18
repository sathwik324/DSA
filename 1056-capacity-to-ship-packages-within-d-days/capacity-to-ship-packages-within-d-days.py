class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        n = len(weights) 
        def can_ship(capacity : int) :
            days_needed = 1 
            curr_load = 0 
            for w in weights:
                if curr_load + w > capacity :
                    days_needed += 1 
                    curr_load = w 
                else : 
                    curr_load += w  
            return days_needed <= days             
          
        left = max(weights)
        right = sum( w for w in weights)
        while left < right :
            mid = (left+right)//2 
            if can_ship(mid) : 
                right = mid 
            else : 
                left = mid+1    
        return left           
