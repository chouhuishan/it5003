import random 

def get_quick_sort(A: list[int], low: int, high: int) -> list[int]:
    if low >= high:
        return A

    r = low + random.randrange(high-low+1) # choose a random pivot and move it toA[low]
    A[low], A[r] = A[r], A[low] 

    p = A[low] # p is the pivot
    m = low 

    for k in range(low+1, high+1):
        if A[k] < p or (A[k] == p and random.randrange(2) == 0):
            m += 1
            A[k], A[m] = A[m], A[k]
    A[low], A[m] = A[m], A[low] # put the pivot into the original position

    get_quick_sort(A, low, m - 1) # recursively sort left sublist
    get_quick_sort(A, m + 1, high) # recursively sort right sublist
    
    return A

A = [27, 38, 12, 39, 29, 16]
print(get_quick_sort(A, 0, len(A) - 1))

# p = A[0] = 27
# swap A[1] = 38 as part of S2 so S1 = {} and S2 = {38}
# swap A[1] = 38 with A[2] = 12 so S1 = {12} and S2 = {38}
# set A[3] = 39 and later A[4] = 29 as part of S2 so S1 = {12} and S2 = {38, 29, 29}
# swap A[2] = 38 with A[5] = 16 so S1 = {12, 16} and S2 = {39, 29, 38}
# swap p with A[2] = 16 so that S1 = {16, 12}, p ={27} and S2 = {39, 29, 38}

# Time Complexity: O(N log N) worst cases for all cases  
# Time Complexity: O(log N) - Rare case when partition splits the array into 2 equal halves 


# Random Quick Sort
# same code above can be used for Random Quick Sort
# Time complexity: O(N log N)