def get_max_time_satisfy_requirements(N, max_time):
    for i in range(N - 2, -1, -1):
        if max_time[i] > max_time[i + 1]:
            max_time[i] = max_time[i + 1]
    return sum(max_time)


N = int(input())  # number of days
max_time = list(map(int, input().split()))

print(get_max_time_satisfy_requirements(N, max_time))


# def get_max_time_satisfy_requirements(N, max_time):
#     total = 0

#     for i in reversed(max_time):
#         time = min(max_time[i], max_time[i + 1])
#         total += time
#     return total


# N = int(input())  # number of days
# max_time = list(map(int, input().split()))

# print(get_max_time_satisfy_requirements(N, max_time))
