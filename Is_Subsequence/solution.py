class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        buffer_t = list(t)
        length_t = len(t)
        length_s = len(s)
        j = 0
        subs = []

        for i in range(length_t):
            if j >= length_s:  
                break          

            if buffer_t[i] == s[j]:
                subs.append(buffer_t[i])
                j+=1
       
        
        final_t = ''.join(subs)
        return s == final_t