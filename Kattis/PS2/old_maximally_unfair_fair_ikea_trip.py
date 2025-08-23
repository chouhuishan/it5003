def get_weight(k: int, n: int, dict_weight_furniture) -> tuple[int, list[str]]:
    if k == 1:
        return sum(dict_weight_furniture.keys()), sorted(dict_weight_furniture.values())
    else:
        min_furnitures = n // k

        weights_ascending_order = sorted(dict_weight_furniture.keys())
        # print(weights_ascending_order)

        total_weight = sum(weights_ascending_order[:min_furnitures])

        if total_weight + weights_ascending_order[min_furnitures] < sum(
            weights_ascending_order[min_furnitures + 1 : min_furnitures * 2 + 1]
        ):
            total_weight += weights_ascending_order[min_furnitures]
            min_furnitures += 1
        return total_weight, sorted(
            [
                dict_weight_furniture[weight]
                for weight in weights_ascending_order[:min_furnitures]
            ]
        )

        # count, total_weight = 0, 0

        # while count < min_number_furnitures_D:
        #     total_weight += weights_ascending_order[count]
        #     count += 1
        #     # print(f"{count=}")

        # if total_weight + weights_ascending_order[count] < sum(
        #     weights_ascending_order[count + 1 : (min_number_furnitures_D + count + 1)]
        # ):
        #     min_number_furnitures_D += 1
        # return sum(weights_ascending_order[:min_number_furnitures_D])


# def parse_furniture_weight(furniture_weight: tuple[str, str]) -> tuple[str, int]:
#     return furniture_weight[0], int(furniture_weight[1])


k = int(input())  # number of people carrying stuff
n = int(input())  # number of furniture items and their weights

# assume each furniture has distinct weight
list_furniture_weight: list[tuple[str, str]] = [input().split() for _ in range(n)]
dict_weight_furniture: dict[int, str] = {int(w): f for f, w in list_furniture_weight}

final_weight, final_furnitures = get_weight(k, n, dict_weight_furniture)
print(final_weight)

for furniture in final_furnitures:
    print(furniture)
