def get_merge_sort(A : list[int]) -> list[int]:
    N = len(A)
    if N <= 1: 
        return A # return the list as it is
    
    mid = N // 2  # split into 2 halves
    left = A[:mid] # [:mid] : from start to before mid    
                   # if N is odd, left is less than right by 1
    right = A[mid:] # [mid:] : from mid to end
    get_merge_sort(left) # recursively sort each half
    get_merge_sort(right)

    i, j, k = 0, 0, 0
    # Merge the two sorted halves back into A
    # i walks left, j walks right, k writes into A
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    # copy any leftovers
    while i < len(left):
        A[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        A[k] = right[j]
        k += 1
        j += 1
    return A

A = [1,5,19,20,2,11,15,17]
print(get_merge_sort(A))

# Time Complexity: O(N log N) for all cases
# Given 2 sorted arrays, the size of N1 & N2, we can efficiently 
# merge them into one larger combined sorted array of Size N = N1 + N2 -- O(N) time complexity
# 