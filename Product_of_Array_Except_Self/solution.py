class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        product_left = [1] * length
        product_right = [1] * length

        for i in range(1, length):
            product_left[i] = product_left[i-1] * nums[i-1]
        
        for i in range(length-2, -1, -1):
            product_right[i] = product_right[i+1] * nums[i+1]
            product_left[i] *= product_right[i]
            
        product_left[length-1] *= product_right[length-1]
        return product_left
        