# Container With Most Water

## Approach

Use the Two-Pointer Approach to find the maximum area of water that can be contained between two lines.

- Initialize two pointers, `i` at the beginning and `j` at the end of the array.
- Calculate the area using the minimum of the two heights multiplied by the distance between the pointers.
- Update the maximum area found so far.
- Move the pointer pointing to the shorter line inward, since moving the taller line cannot increase the area.
- Repeat until the two pointers meet, then return the maximum area.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

where `n` is the length of the `height` array.

## Stats

- **Runtime:** 52ms (Beats: 79.09%)
- **Memory:** 29.68MB (Beats: 39.37%)