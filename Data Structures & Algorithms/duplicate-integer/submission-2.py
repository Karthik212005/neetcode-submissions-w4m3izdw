class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        xor=0
        nums.sort()
        if len(nums)==1:
            return False
        for i in range(len(nums)):
            
            xor=nums[i]^nums[i-1]
            
            if xor==0:
                return True
        return False

        