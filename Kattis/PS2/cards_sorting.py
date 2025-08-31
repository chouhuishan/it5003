def get_cards_sorted(
    list_cards: list[dict[str, str | tuple[str, str]]], sort_orders: list[str]
) -> list[str]:
    card_types = {
        "Skrimsli": 0,
        "Galdur": 1,
        "Gildra": 2,
        "Annad": 3,
    }

    subcard_types = {
        "Skrimsli": {
            "Venjulegt": 0,
            "Ahrifa": 1,
            "Bodunar": 2,
            "Samruna": 3,
            "Samstillt": 4,
            "Thaeo": 5,
            "Penduls": 6,
            "Tengis": 7,
        },
        "Galdur": {
            "Venjulegur": 0,
            "Bunadar": 1,
            "Svida": 2,
            "Samfelldur": 3,
            "Bodunar": 4,
            "Hradur": 5,
        },
        "Gildra": {"Venjuleg": 0, "Samfelld": 1, "Mot": 2},
        "Annad": {},
    }

    def sort_key(
        card: dict[str, str | tuple[str, str]],
    ) -> tuple[
        str | tuple[int, int],
        str | tuple[int, int],
        str | tuple[int, int],
        str | tuple[int, int],
    ]:
        # card = {
        #    "nafn": 'Graedgiskrukka',
        #    "id": "55144522",
        #    "flokkur": ('Galdur', 'Venjulegur'),
        #    "dagsetning" : '2004-03-01'
        # }
        # sort_order = ["flokkur", "dagsetning", "nafn", "id"]
        # return ((1, 0), '2004-03-01', 'Graedgiskrukka', "55144522")

        # initialzed with original list
        naturally_sorted = list(card.values())

        for i, key in enumerate(sort_orders):
            if key == "flokkur":
                if card[key][0] == "Annad":
                    naturally_sorted[i] = (card_types[card[key][0]], 0)
                else:
                    naturally_sorted[i] = (
                        card_types[card[key][0]],
                        subcard_types[card[key][0]][card[key][1]],
                    )
            else:
                naturally_sorted[i] = card[key]

        return tuple(naturally_sorted)

    list_cards_sorted = sorted(list_cards, key=sort_key)

    return [card["nafn"] for card in list_cards_sorted]


def process_list_cards(
    list_cards_raw: list[tuple[str, str, str, str]],
) -> list[dict[str, str | tuple[str, str]]]:
    # [('Graedgiskrukka', '55144522', 'Galdur - Venjulegur', '2004-03-01')]
    # => [{
    #    "nafn": 'Graedgiskrukka',
    # .   "id": "55144522",
    # .   "flokkur": ('Galdur', 'Venjulegur'),
    #    "dagsetning" : '2004-03-01'
    # },...]

    list_cards = []

    for card in list_cards_raw:
        card_dict = {}
        card_dict["nafn"] = card[0]
        card_dict["id"] = card[1]
        card_dict["flokkur"] = tuple(card[2].split(" - "))
        card_dict["dagsetning"] = card[3]
        list_cards.append(card_dict)

    return list_cards


n = int(input())

list_cards_raw: list[tuple[str, str, str, str]] = [
    tuple(input().split(", ")) for _ in range(n)
]
sort_orders = input().split()
list_cards = process_list_cards(list_cards_raw)

print("\n".join(get_cards_sorted(list_cards, sort_orders)))
