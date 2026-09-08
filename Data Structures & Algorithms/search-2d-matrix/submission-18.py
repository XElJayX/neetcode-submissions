class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])-1
        print(m,n)
        l,r,row = 0,n,0
        for i in range(m):
            print(matrix[i][n])
            if matrix[i][n] >= target:
                row = i
                print("Found")
                break
        if matrix[row][0] == target or matrix[row][n] == target:
            return True

        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid +1
            else:
                r = mid -1
        return False

        #matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        # matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]


