class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        res_arr = [] 
        n = len(arr) 
        h = 0 
        for i in range (1,n+k+1) :
            if h >= n  or arr[h] != i  :
                res_arr.append(i) 
            else : 
                h += 1    
        return res_arr[k-1] 
             