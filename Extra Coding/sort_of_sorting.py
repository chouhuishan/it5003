while True:
    n = int(input())
    if n == 0:
        break

    # names = [] this is the second way
    # for i in range(n):
    #     names.append(input())
    # name = input() this is the long way
    # names.append(name)

    names = [input() for _ in range(n)]  # this is the third way, which is the shortest
    names.sort(key=lambda name: name[:2])
    print(*(names + [""]), sep="\n")  # for i in range(n):
    #     print(names[i])
