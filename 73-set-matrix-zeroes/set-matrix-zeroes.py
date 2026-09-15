class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_rows = set() 
        zero_cols = set() 
        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 0 :
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in zero_rows :
            matrix[i] = [0] * n             
        for c in zero_cols :
            for j in range(m) :
                matrix[j][c] = 0 

                    



        