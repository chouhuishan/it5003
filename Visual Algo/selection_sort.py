def get_selection_sort(A: list[int]) -> list[int]:
    for i in range(len(A) - 1):
        smallest = i + A[i:].index(min(A[i:]))
        A[smallest], A[i] = A[i], A[smallest]
    return A


A = [29, 10, 14, 37, 14]
print(get_selection_sort(A))
# note that if there is a duplicate, the one on the left will remain untouched


# Time Complexity: O(N**2) for all cases

# NO NEED TO CHECK if A[smallest] < A[i], because smalle sis by construction of the
# index of the minimum value -> A[smallest] m < A[i] ALWAYS

# A[i:] slices from position i to the end
# min(A[i:]) : the smallest value in the slice
# A[i:].index(min(A[i:]) : index of the smallest value
# smallest = i + A[i:].index(min(A[i:])) : absolute index of the samllest element
