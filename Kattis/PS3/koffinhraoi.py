# Matric Number : A0190163L
# Full name : Chou Hui Shan
# Lab : B1
# Lab group TA : Jeanette Tan Yu Wei

import heapq


def how_many_drinks(n, task: list[tuple[int, int]]) -> int:
    task_sorted = sorted(task, key=lambda x: x[1])

    total_hours = 0
    drinks = 0
    hours_each_task = []

    for h, d in task_sorted:  # h = hours needed, d = deadline
        total_hours += h
        # heapq.heapify(hours_each_task) - see below for comments
        heapq.heappush(hours_each_task, -h)

        while total_hours > d:
            max_hour_in_heap = -heapq.heappop(hours_each_task)
            new_duration = max_hour_in_heap // 2
            total_hours = total_hours - max_hour_in_heap + new_duration
            heapq.heappush(hours_each_task, -new_duration)

            drinks += 1

    return drinks


n = int(input())
task = [tuple(map(int, input().split())) for _ in range(n)]
print(how_many_drinks(n, task))


# heapify - no need to heapify as we start from an empty list
#           useful if we start from a pre-filled list
#           since the list is empty, heapify every iteration adds every extra O(k),
#           turnning the algo to O(n**2)
