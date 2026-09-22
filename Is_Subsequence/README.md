# Is Subsequence

## Approach

Use a two-pointer approach to check whether `s` appears as a subsequence of `t`.

- Traverse through `t` using a loop.
- Compare each character of `t` with the current character of `s`.
- When they match, add the character to `subs` and move the pointer for `s`.
- Finally, join the matched characters and compare them with `s`.

## Complexity

- **Time:** `O(n + m)`

- **Space:** `O(n + m)`

where `n` and `m` are the lengths of `s` and `t`.

## Stats

- **Runtime:** `1ms` (Beats: 34.56%)

- **Memory:** `19.46MB` (Beats: 7.97%)