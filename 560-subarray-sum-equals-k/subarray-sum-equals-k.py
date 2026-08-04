class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
        count = defaultdict(int) 
        count[0] = 1 
        result = 0 
        curr_sum = 0 
        for num in nums :
            curr_sum += num 
            result += count[curr_sum - k] 
            count[curr_sum] += 1 
        return result        


        






        
        