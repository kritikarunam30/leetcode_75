# 1431. Kids With the Greatest Number of Candies

## Approach

Find the greatest number of candies among all the kids, then check each kid individually after adding all the `extraCandies`.

- Calculate the maximum value in `candies`.
- For each kid, add `extraCandies` to their current candies.
- If the resulting number is greater than or equal to the maximum, append `True`.
- Otherwise, append `False`.
- Return the resulting boolean array.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

where `n` is the number of kids.

## Stats

- **Runtime:** 0ms (Beats: 100.00%)
- **Memory:** 19.14MB (Beats: 90.86%)