class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False     
        temp = [0] * 26

        for i in range(len(s)):
            temp[ord(s[i])-ord('a')]=temp[ord(s[i])-ord('a')]+1
            temp[ord(t[i])-ord('a')]=temp[ord(t[i])-ord('a')]-1

        for i in range(26):
            if temp[i]!=0:
                return False

        return True            

            


        