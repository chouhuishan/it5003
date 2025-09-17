# Matric Number : A0190163L
# Full name : Chou Hui Shan
# Lab : B1
# Lab group TA : Jeanette Tan Yu Wei

import sys


def get_original_message(n: int) -> str:
    duplicates = {}
    message_stack = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip("\n")
        if line not in duplicates:
            reversed_line = line[::-1]
            duplicates[line] = reversed_line
        else:
            reversed_line = duplicates[line]

        message_stack.append(reversed_line)

    correct_order = []
    while message_stack:
        correct_order.append(message_stack.pop())

    return "".join(correct_order)


n = int(input())  # number of notes
print(get_original_message(n))
