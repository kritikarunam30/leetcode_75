class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        j = 0
        length = len(nums)-1
        
        while j < length:
            while nums[i] != 0 and i < length:
                i += 1
            while nums[j] == 0 and j < length:
                j += 1
            
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j = i