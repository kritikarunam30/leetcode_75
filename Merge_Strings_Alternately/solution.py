class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        length = max(len(word1), len(word2))
        i = 0
        
        while i < length:
            try:
                merged.append(word1[i])
            except Exception:
                merged.append(word2[i:])
                break
            try:
                merged.append(word2[i])
            except Exception:
                if i+1 < length:
                    merged.append(word1[i+1:])
                break

            i += 1

        return ''.join(merged)