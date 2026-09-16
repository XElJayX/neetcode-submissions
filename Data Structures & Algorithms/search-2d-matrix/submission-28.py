class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) -1 
        row = 0       
        for i in range(m):
            if target == matrix[i][n]:
                return True
            elif target > matrix[i][n]:
                print(matrix[i][n])
                print("iteration DEBUG:",i)
                continue   
            else:
                row = i
                print("row found:",row)
                break

        l,r = 0, n
        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid -1
            else:
                l = mid +1
                    
                
        return False

                    

