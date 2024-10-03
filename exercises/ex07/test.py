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


def get_weather_report() -> str:
    weather: str = input("What is the weather? ")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")

    return weather


get_weather_report()
