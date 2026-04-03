class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(n):
            if nums[i]==nums[i-1] and i>0:
                continue
            j=i+1
            k=n-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif s<0:
                    j+=1
                else:
                    k-=1
        return res
                    

        