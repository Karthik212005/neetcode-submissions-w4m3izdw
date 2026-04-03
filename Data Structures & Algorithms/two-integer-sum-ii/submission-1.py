class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        
        n=len(num)
        l=1
        r=n
        res=[]
        while l<r:
            s=num[l-1]+num[r-1]
            if s==target:
                res.append([l,r])
                l+=1
                r-=1
            elif s<target:
                l+=1
            else:
                r-=1
        return res[0]
                