# Product of Array Except Self

## Approach

Use separate arrays to store the cumulative product of elements to the left and right of each index.

- First, build `product_left`, where `product_left[i]` stores the product of all elements before index `i`.
- Then, traverse from right to left and build `product_right`, where `product_right[i]` stores the product of all elements after index `i`.
- Multiply `product_left[i]` by `product_right[i]` to get the product of all elements except `nums[i]`.
- Reuse `product_left` to store the final answer instead of creating another array.

## Complexity

- **Time:** `O(n)`

- **Space:** `O(n)`

where `n` is the length of `nums`.

## Stats

- **Runtime:** 32ms (Beats: 28.57%)

- **Memory:** 27.24MB (Beats: 28.21%)