# 1768. Merge Strings Alternately

## Approach

Iterate through both strings simultaneously and add their characters alternately to a list.

- Continue until the longer string is exhausted.
- If one string ends first, append the remaining characters of the other string.
- Join the list at the end to form the result.

## Complexity

- **Time:** `O(n + m)`
- **Space:** `O(n + m)`

where `n` and `m` are the lengths of `word1` and `word2`.

## Stats

-**Runtime:** 48ms (Beats: 37.40%)
-**Memory:** 19.30MB (Beats: 56.87%)