**# Move Zeroes**

**## Approach**

Use two pointers to move all zeroes to the end of the array while maintaining the relative order of the non-zero elements.

- `i` searches for the next zero that needs to be moved.

- `j` searches for the next non-zero element after the zero.

- When `i < j`, swap `nums[i]` and `nums[j]` to move the non-zero element forward.

- Continue until all elements have been processed.

**## Limitation**

- This approach uses nested `while` loops to repeatedly search for zero and non-zero elements, making the pointer movement more complicated than necessary.

- Although the theoretical complexity is `O(n)`, the implementation performs more scanning and swapping than a simpler two-pointer approach.

- A single-pass two-pointer solution can achieve the same `O(n)` time and `O(1)` space complexity with simpler logic and better practical performance.

**## Alternate Solution**

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
```

**## Complexity**

- **Time:** `O(n)`

- **Space:** `O(1)`

where `n` is the length of `nums`.

**## Stats**

- **Runtime:** 2350ms (Beats: 5.01%)

- **Memory:** 20.45MB (Beats: 62.68%)