import sys
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        i = 0
        if len(s)!=len(t):
            return False
            exit()
        while i<len(s):
            freq[s[i]]= freq.get(s[i],0)+1
            freq[t[i]] = freq.get(t[i],0)-1
            i+=1
        for val in freq.values():
            if val!=0:
                return False
                break
        return True


