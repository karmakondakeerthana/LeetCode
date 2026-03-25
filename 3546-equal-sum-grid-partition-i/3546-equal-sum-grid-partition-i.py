class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        total_sum=sum(sum(row) for row in grid)
        if total_sum%2!=0:
            return False
        target=total_sum//2
        current_sum=0
        for i in range(m-1):
            current_sum+=sum(grid[i])
            if current_sum==target:
                return True
        current_sum=0
        col_sum=[0]*n
        for j in range(n):
            for i in range(m):
                col_sum[j]+=grid[i][j]
        for j in range(n-1):
            current_sum+=col_sum[j]
            if current_sum==target:
                return True
        return False
        