def get_insertion_sort(A: list[int]) -> list[int]:
    N = len(A)
    for i in range(1, N):
        x = A[i]  # this is the key
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = x
    return A


A = [29, 10, 14, 37, 14]
print(get_insertion_sort(A))


# Time complexity:  O(N**2) -> Worse case scenario
# Time Complexity : O(N) -> Best case scenario


# at step i, we take the key and shift any larger elements in A[:i]
# one position to the right and insert x into the hole made
