```md
# 345. Reverse Vowels of a String

## Approach

Use the **two-pointer technique** to find vowels from both ends of the string and swap them.

- Convert the string into a list so that its characters can be modified.
- Initialize two pointers:
  - `i` at the beginning of the string.
  - `j` at the end of the string.
- Move `i` forward until it points to a vowel.
- Move `j` backward until it points to a vowel.
- Swap the vowels at `i` and `j`.
- Continue until the two pointers meet.
- Join the list back into a string and return the result.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

where `n` is the length of the string.

## Stats

- **Runtime:** 15ms (Beats: 31.76%)
- **Memory:** 20.57MB (Beats: 51.96%)
```
