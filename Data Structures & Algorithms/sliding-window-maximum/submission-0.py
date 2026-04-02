class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        curr=max(nums[:k])
        res=[]
        res.append(curr)
        for i in range(1,n-k+1):
            curr=max(nums[i:i+k])
            res.append(curr)
        return res


