class Solution:
    def maxArea(self, he: List[int]) -> int:
        maxa=0
        n=len(he)
        l=0
        r=n-1
        while l<r:
            h=min(he[l],he[r])
            w =r-l
            a=w*h
            maxa=max(maxa,a)
            if he[l]<=he[r]:
                l+=1
            else:
                r-=1
        return maxa

