class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        min_dist=float('inf')
        for i in range(n):
            if words[i]==target:
                diff=abs(i-startIndex)
                dist=min(diff,n-diff)
                min_dist=min(min_dist,dist)
        return min_dist if min_dist!=float('inf') else-1
        