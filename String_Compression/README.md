# String Compression

## Approach

Use two pointers, `read` and `write`, to identify consecutive groups of identical characters and compress them in place.

- Traverse the array using `read` to find consecutive groups of the same character.
- Count the occurrences of each character and convert the count to a string when it is greater than 1.
- Write the count digits into the array, handling both single-digit and multi-digit counts.
- Remove redundant characters using `pop()` to maintain the compressed array.
- Update the array length after each group and return the final length.

The optimal solution uses two pointers to overwrite the original array with compressed characters and counts, avoiding repeated deletions and achieving linear time complexity.

## Complexity

- **Time:** `O(n^2)` in the worst case due to repeated `pop()` operations and shifting elements.
- **Space:** `O(n)` in the worst case due to temporary digit lists.

where `n` is the length of the input array.

## Stats

- **Runtime:** 2ms (Beats: 51.20%)
- **Memory:** 19.25MB (Beats: 86.45%)