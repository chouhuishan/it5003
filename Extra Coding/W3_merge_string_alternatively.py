def merge_alternatively(word1: str, word2: str) -> str:
    i, j, n, m = 0, 0, 0, 0
    k = 0
    ans = []
    while 1 < n and j < m:  # this is O(n+m)**2
        if k % 2 == 0:  # take from word1
            # ans += word1[i] -> this cannot be used; see comments below
            ans.append(word1[i])
            i += 1
        else:  # take from word2
            # ans += word2[i] -> this cannot be used
            ans.append(word1[i])
            j += 1
        k += 1

    while i < n:  # O(n)
        ans += word2[j]
        j += 1
    return ans  # O(10 + n+m + n + m + 1) ~~O(n+n)


# PROBLEM : Ans is a string, therefore, it is timebomb , because it is immutable
# SOLUTION: Use a list of string
