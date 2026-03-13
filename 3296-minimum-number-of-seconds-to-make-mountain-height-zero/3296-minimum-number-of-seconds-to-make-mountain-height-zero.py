class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def canFinish(T):
            total=0
            for t in workerTimes:
                left,right=0,mountainHeight
                best=0
                while left<=right:
                    mid=(left+right)//2
                    time=t*mid*(mid+1)//2
                    if time<=T:
                        best=mid
                        left=mid+1
                    else:
                        right=mid-1
                total+=best
                if total>=mountainHeight:
                    return True
            return False
        left,right=0,10**18
        while left<right:
            mid=(left+right)//2
            if canFinish(mid):
                right=mid
            else:
                left=mid+1
        return left
        