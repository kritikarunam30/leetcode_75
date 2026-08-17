class Solution:
    def alldivisors(self, len1, len2) -> list:
        divisors = []
        for i in range(len2, 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                divisors.append(i)
        
        return divisors

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #var1 is greater in length
        len1 = len(str1)
        len2 = len(str2)

        #checking if len1 is greater else swap
        if len1 < len2:
            str1, str2 = str2, str1
            len1, len2 = len2, len1
        
        divisors = self.alldivisors(len1, len2)

        for divisor in divisors:
            subs = ''.join(str2[0:divisor])
            sub1 = subs * (len1 // divisor)
            sub2 = subs * (len2 // divisor)

            if sub1 == str1 and sub2 == str2:
                return subs

        return ""