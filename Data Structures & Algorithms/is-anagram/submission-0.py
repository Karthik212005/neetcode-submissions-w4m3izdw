class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # freq1={}
        # freq2={}
        # if len(s)!=len(t):
        #     return False
        # for i in range(len(s)):
        #     freq1[s[i]]+=1
        #     freq2[t[i]]+=1
        # freq1.sort()
        # freq2.sort()
        # return freq1==freq2
        return sorted(s)==sorted(t)
        