# 605. Can Place Flowers

## Approach

Iterate through the flowerbed and check whether a flower can be placed at each empty position.

- For each position, check the adjacent positions using the `condition` helper method.
- Treat the position before the first element and the position after the last element as `0`.
- If both adjacent positions are empty, place a flower and decrease `n`.
- Stop iterating once all `n` flowers have been placed.
- Return `True` if all required flowers are placed; otherwise, return `False`.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

where `n` is the length of the flowerbed.

## Stats

- **Runtime:** 3ms (Beats: 97.05%)
- **Memory:** 19.46MB (Beats: 78.31%)