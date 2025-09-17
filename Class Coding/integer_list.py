from collections import deque

num_test_cases = int(input())  # number of test cases

for _ in range(num_test_cases):
    operations = input()
    n = int(input())
    lst = input().strip("[]")
    if lst:
        lst = lst.split(",")
    else:
        lst = []
    lst = deque(lst)

    is_reversed = False
    for operation in operations:
        if operation == "R":  # if R, set reversed status
            lst = not is_reversed
        else:
            if not lst:
                print("error")
                break
            else:
                if is_reversed:
                    lst.pop()
                else:
                    lst.popleft()
            # if D, drop either first or last
            # if lst is emoty, output error
    else:
        if is_reversed:
            lst.reverse()
        print("[" + ",".join(lst) + "]")

# if there is no 'error' output lst
