class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        text = s.lower()
        end = len(text) - 1
        flag = True
        while start < end:
            if not text[start].isalnum():
                start+=1
                continue
            if not text[end].isalnum():
                end-=1
                continue
            print("DEBUG: ", text[start], text[end])
            if text[start] != text[end]:
                flag = False
                break
            start+=1
            end-=1

        return flag