from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups=defaultdict(list)
        for i,num in enumerate(nums):
            groups[num].append(i)
        n=len(nums)
        res=[0]*n
        for indices in groups.values():
            k=len(indices)
            prefix=[0]*(k+1)
            for i in range(k):
                prefix[i+1]=prefix[i]+indices[i]
            for i in range(k):
                idx=indices[i]
                left=i*idx-prefix[i]
                right=(prefix[k]-prefix[i+1])-(k-i-1)*idx
                res[idx]=left+right
        return res