def get_asc_weight(
    list_furniture_weight: list[tuple[str, int]],
) -> list[tuple[str, int]]:
    list_with_index = [
        (name, weight, index)
        for index, (name, weight) in enumerate(list_furniture_weight)
    ]
    # NOTE: sort by both weight and orignal index
    #       primary sort key: weight
    #       secondary sort key: index
    list_with_index_sorted = sorted(list_with_index, key=lambda t: (t[1], t[2]))

    return [(name, weight) for name, weight, _ in list_with_index_sorted]


def get_total_weight(list_furniture_weight: list[tuple[str, int]]) -> int:
    return sum(weight for _, weight in list_furniture_weight)


def get_sorted_furniture(list_furniture_weight: list[tuple[str, int]]) -> list[str]:
    return sorted([name for name, _ in list_furniture_weight])


def get_furnitures_carried(
    k: int, n: int, list_furniture_weight: list[tuple[str, int]]
) -> tuple[int, list[str]]:
    if k == 1:
        return get_total_weight(list_furniture_weight), get_sorted_furniture(
            list_furniture_weight
        )

    list_ascending_weight = get_asc_weight(list_furniture_weight)

    # NOTE: when number of furniture need to be carried is equal
    num_furniture = n // k
    list_carried = list_ascending_weight[:num_furniture]
    if n % k != 0:
        # NOTE: check if adding one more is less than next batch
        list_carried_additional = list_ascending_weight[: num_furniture + 1]
        if get_total_weight(list_carried_additional) < get_total_weight(
            list_ascending_weight[num_furniture + 1 : num_furniture * 2 + 1]
        ):
            list_carried = list_carried_additional

    return get_total_weight(list_carried), get_sorted_furniture(list_carried)


k = int(input())  # number of people carrying stuff
n = int(input())  # number of furniture items and their weights

cast_weight_in_tuple = lambda name, weight_str: (name, int(weight_str))

list_furniture_weight: list[tuple[str, int]] = [
    cast_weight_in_tuple(*input().split()) for _ in range(n)
]

final_weight, final_furnitures = get_furnitures_carried(k, n, list_furniture_weight)
print(final_weight)
for furniture in final_furnitures:
    print(furniture)
