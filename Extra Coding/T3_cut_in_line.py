# N = int(input())
# line = [input() for _ in range(N)]

# C = int(input())
# for _ in range(C):
#     event = input()
#     if "cut" in event:  # if event[0] == 'c'        a, b = event.split()[1:]
#         pos = line.index(b)
#         line.insert(pos, a)
#     else:
#         a = event.split()[1]
#         line.remove(a)


def get_names(line: list[str], events: list[str]) -> list[str]:
    for event in events:
        parts = event.strip().split()
        if parts[0] == "cut":
            _, a, b = parts
            position_original_person = line.index(b)
            line.insert(position_original_person, a)  # list.insert(index, element),
        # putting the queue cutter into the original person po
        else:  # leave the queue
            _, a = parts
            line.remove(a)
    return line


N = int(input())
line = [input() for _ in range(N)]
C = int(input())
events = [input() for _ in range(C)]
for name in get_names(line, events):
    print(name)
