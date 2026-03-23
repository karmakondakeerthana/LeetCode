class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD=1000000007
        m=len(grid)
        n=len(grid[0])
        dp_max=[]
        dp_min=[]
        for i in range(m):
            dp_max.append([0]*n)
            dp_min.append([0]*n)
        dp_max[0][0]=grid[0][0]
        dp_min[0][0]=grid[0][0]
        for j in range(1,n):
            dp_max[0][j]=dp_max[0][j-1]*grid[0][j]
            dp_min[0][j]=dp_min[0][j-1]*grid[0][j]
        for i in range(1,m):
            dp_max[i][0]=dp_max[i-1][0]*grid[i][0]
            dp_min[i][0]=dp_min[i-1][0]*grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                val=grid[i][j]
                a=dp_max[i-1][j]*val 
                b=dp_min[i-1][j]*val
                c=dp_max[i][j-1]*val
                d=dp_min[i][j-1]*val
                dp_max[i][j]=max(a,b,c,d)
                dp_min[i][j]=min(a,b,c,d)
        result=dp_max[m-1][n-1]
        if result<0:
            return -1
        return result%MOD  