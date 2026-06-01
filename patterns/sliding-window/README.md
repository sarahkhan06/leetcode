# Sliding Window Pattern

## When to use
- Subarray / substring problems
- "Longest / shortest ... that satisfies condition"
- Contiguous sequence problems

## Template
```python
def sliding_window(s):
    left = 0
    window = {}
    result = 0

    for right in range(len(s)):
        # 1. Expand — add s[right]
        window[s[right]] = window.get(s[right], 0) + 1

        # 2. Shrink — while invalid
        while INVALID_CONDITION:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        # 3. Update result
        result = max(result, right - left + 1)

    return result
```

## Problems to solve
- [ ] #3 Longest Substring Without Repeating Characters
- [ ] #76 Minimum Window Substring
- [ ] #239 Sliding Window Maximum
- [ ] #424 Longest Repeating Character Replacement
- [ ] #567 Permutation in String
