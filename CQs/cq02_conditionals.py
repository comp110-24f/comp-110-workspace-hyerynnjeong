__author__ = "730813516"


def guess_a_number() -> None:
    secret: int = 7
    guess = int(input("Guess a number: "))
    print("Your guess was", guess)
    if secret == guess:
        print("You got it!")
    elif secret > guess:
        print("Your guess was too low! The secret number is", secret)
    else:
        print("Your guess was too high! The secret number is", secret)
    return None


if __name__ == "__main__":
    guess_a_number()
