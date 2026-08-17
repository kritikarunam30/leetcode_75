# 1071. Greatest Common Divisor of Strings

## Approach

Find all common divisors of the lengths of `str1` and `str2`, starting from the largest possible divisor.

- Ensure `str1` is the longer string.
- Generate all common divisors of the two string lengths in descending order.
- For each divisor, take the corresponding prefix from `str2` as the candidate substring.
- Repeat the candidate enough times to reconstruct both strings.
- Return the first candidate that forms both strings completely.

Since the divisors are checked from largest to smallest, the first valid candidate is the greatest common divisor string.

## Complexity

- **Time:** `O(n + m + min(n, m))`
- **Space:** `O(min(n, m))`

where `n` and `m` are the lengths of `str1` and `str2`.

## Stats

- **Runtime:** 0ms (Beats: 100.00%)
- **Memory:** 19.48MB (Beats: 8.56%)