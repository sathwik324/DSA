class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def can_make_bouquets(days: int) -> bool:
            bouquets = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0  
                else:
                    flowers = 0      
                    
            return bouquets >= m

        left = min(bloomDay)
        right = max(bloomDay)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            
            if can_make_bouquets(mid):
                ans = mid
                right = mid - 1 
            else:
                left = mid + 1   

        return ans

        