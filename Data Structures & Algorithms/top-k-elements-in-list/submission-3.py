from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        arr=[]
        freq=defaultdict(int)
        for i in nums:
            freq[i]+=1
        for i,val in freq.items():
            arr.append([i,val])
        arr.sort(key=lambda x: x[1] )
        while len(res)<k:
            res.append(arr.pop()[0])
           

            
        return res
