def longest_consecutive(nums: list[int]) -> int:
    if nums == []:
        return 0
    s = set(nums)  # convert list into set
    # if value in s OR if v in nums : this is O(n)
    ans = 1
    for n in s: #ignore duplicates
        if n-1 in s:
        l = 1
        next_n = n + 1
        while next_n in s:
            l += 1
            next_n += 1
            ans = max(ans, l)
    return ans
