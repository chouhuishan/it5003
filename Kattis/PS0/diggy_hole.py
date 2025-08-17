def num_of_hours(n, h, x, m, y):
    # total_man_hours = n * h
    # man_hour_per_meter = total_man_hours / x
    # total_man_hours_B = man_hour_per_meter * y
    # num_hours = total_man_hours_B / m

    num_hours = ((n * h / x) * y) / m

    print(num_hours)


n = int(input())  # number of workers in scenario A
h = int(input())  # number of hours in A
x = int(input())  # cubic meters in A
m = int(input())  # number of workers in scenario B
y = int(input())  # cubic meters in B

num_of_hours(n, h, x, m, y)
