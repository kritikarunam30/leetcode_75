class Solution:
    def condition(self, flowerbed, index):
        before = flowerbed[index - 1] if index > 0 else 0
        after = flowerbed[index + 1] if index < len(flowerbed)-1 else 0
        
        if before == 0 and after == 0:
            return True
        return False
    
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        
        for i in range(length):
            if n != 0:
                if flowerbed[i]==0 and self.condition(flowerbed, i):
                        flowerbed[i] = 1
                        n -= 1
            else:
                break
        
        if n == 0:
            return True
        return False
