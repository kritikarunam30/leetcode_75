# 151. Reverse Words in a String

## Approach

Use Python's built-in string methods to remove extra spaces, split the string into words, reverse their order, and join them back together.

- Use `strip()` to remove leading and trailing spaces.
- Use `split(' ')` to separate the words.
- Reverse the list of words using slicing.
- Join the words using a single space.
- Use `re.sub()` to replace multiple consecutive spaces with a single space.
- Fun Fact: Python's `split()` without any arguements handles multiple spaces. A better solution wouldn't require regular expressions (re module).

## Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

where `n` is the length of the input string.

## Stats

- **Runtime:** 3ms (Beats: 30.76%)
- **Memory:** 19.36MB (Beats: 40.20%)