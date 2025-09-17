from collections import deque


def get_original_message(n: int) -> str:
    words = deque()
    for _ in range(n):
        line = input()  # text written on each note
        words.appendleft(line[::-1])
    message = "".join(words)
    return message


n = int(input())  # number of notes
print(get_original_message(n))


def get_original_message(n: int) -> str:
    message = []
    for _ in range(n):
        line = input()  # text written on each note
        reversed_line = line[::-1]
        message.append(reversed_line)
    original_message = "".join(reversed(message))
    return original_message


n = int(input())  # number of notes
print(get_original_message(n))


def get_original_message(n: int) -> str:
    original_message = ""
    for _ in range(n):
        line = input()
        reversed_line = line[::-1]
        original_message = reversed_line + original_message
    return original_message


n = int(input())  # number of notes
print(get_original_message(n))


def get_original_message(n: int) -> str:
    message = []
    for _ in range(n):
        line = input()
        reversed_line = line[::-1]
        message.append(reversed_line)

    correct_order = reversed(message)
    original_message = "".join(correct_order)
    return original_message


n = int(input())  # number of notes
print(get_original_message(n))


def get_original_message(message_list: list[str]) -> str:
    message = []

    for line in message_list:
        message.append(line[::-1])
    correct_order_list = reversed(message)
    return "".join(correct_order_list)


n = int(input())
message_list = [input() for _ in range(n)]


def get_original_message(message_list: list[str]) -> str:
    message = []

    for line in message_list:
        message.append(line[::-1])

    correct_order = []

    while message:
        correct_order.append(message.pop())
    return "".join(correct_order)


n = int(input())
message_list = [input() for _ in range(n)]
print(get_original_message(message_list))


def get_original_message(n: int) -> str:
    duplicates = {}
    original_message = ""
    for _ in range(n):
        line = input()
        if line not in duplicates:
            reversed_line = line[::-1]
            duplicates[line] = reversed_line
        else:
            reversed_line = duplicates[line]
        original_message = reversed_line + original_message
    return original_message


n = int(input())  # number of notes
print(get_original_message(n))

from collections import deque


def get_original_message(n: int) -> str:
    duplicates = {}
    correct_order_list = deque()
    for _ in range(n):
        line = input()
        if line not in duplicates:
            reversed_line = line[::-1]
            duplicates[line] = reversed_line
        else:
            reversed_line = duplicates[line]

        correct_order_list.appendleft(reversed_line)

    return "".join(correct_order_list)


n = int(input())  # number of notes
print(get_original_message(n))
