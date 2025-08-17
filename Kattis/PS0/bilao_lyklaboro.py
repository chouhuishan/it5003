def remove_duplicate(s: str) -> str:
    deduped = s[0]

    for i in range(1, len(s)):
        if s[i] != deduped[-1]:
            deduped += s[i]

    return deduped


s = input().lower()

print(remove_duplicate(s))
