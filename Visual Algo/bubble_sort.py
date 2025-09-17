def get_bubble_sort(A: list[int]) -> list[int]:
    N = len(A)
    while N > 1:
        swapped = False  # creating a boolean flag named swapped and set it to False
        for i in range(
            N - 1
        ):  # at the start of each pass, assumption : no  swaps will happen
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True  # if adjacent pair is swapped, set the swapped = True
        if not swapped:  # after the pass, if it is still False, the list already sorted, so can stop early
            break
        N -= 1
    return A


# Time Complexity : O(N**2) -> Worse case scenario
# Time Complexity : O(N) -> Best case scenario

A = [29, 10, 14, 37, 14]
print(get_bubble_sort(A))
