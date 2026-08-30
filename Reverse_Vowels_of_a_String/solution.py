class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        s = list(s)

        vowels = ['a', 'e', 'i', 'o', 'u']

        while i < j:
            while s[i].lower() not in vowels and i < j:
                i += 1
            while s[j].lower() not in vowels and j > i:
                j -= 1

            if s[i].lower() in vowels and s[j].lower() in vowels:
                s[i], s[j] = s[j], s[i]

            i += 1
            j -= 1
        
        
        return ''.join(s)