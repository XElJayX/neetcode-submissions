class Solution:
    
    def conMap(self, s:str) -> dict[str,int]:
        result = {}
        for char in s:
            if char in result:
                result[char]+=1
            else:
             result[char] = 1
        return result
    
    def isAnagram(self, s: str, t: str) -> bool:
        if self.conMap(s) == self.conMap(t):
            return True
        else:
            return False