def add(one: int, two: int) -> int:
    result = one + two
    return result


add(3, 56)


def check_first_letter(word: str, letter: str) -> None:
    if word[0] == letter:
        print("match!")
    else:
        print("no match!")


check_first_letter("happy", "h")
check_first_letter("happy", "s")
