class Solution:
    def reverseWords(self, s: str) -> str:
        buffer = s.strip().split(' ')

        buffer = buffer[-1::-1]
        buffer = ' '.join(buffer)

        return re.sub(r'\s{2,}', ' ',buffer)
