class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        res_arr = [] 
        n = len(arr) 
        j = 0 
        for i in range (1,n+k+1) :
            if j >= n  or arr[j] != i  :
                res_arr.append(i) 
            else : 
                j += 1    
        return res_arr[k-1] 
             