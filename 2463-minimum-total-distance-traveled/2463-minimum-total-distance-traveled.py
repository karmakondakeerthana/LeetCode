class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()    
        from functools import lru_cache  
        m, n = len(robot), len(factory)
        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return 0
            if j == n:
                return float('inf')
            res = dp(i, j + 1) 
            pos, limit = factory[j]
            cost = 0
            for k in range(1, min(limit, m - i) + 1):
                cost += abs(robot[i + k - 1] - pos)
                res = min(res, cost + dp(i + k, j + 1))     
            return res  
        return dp(0, 0)