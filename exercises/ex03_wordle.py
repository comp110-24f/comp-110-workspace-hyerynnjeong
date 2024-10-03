"""Building structured Wordle"""

__author__ = "730813516"


def input_guess(lenword: int) -> str:
    """enter a guess and continue prompting them until they provide a guess of
    the correct length"""
    inputword: str = input(f"Enter a {lenword} character word: ")
    while len(inputword) != lenword:
        inputword = input(f"That wasn't {lenword} chars! Try again: ")
        # recollect the inputword which would go through while loop
    return inputword


def contains_char(secret_word: str, char_guess: str) -> bool:
    """test each index of the first parameter string to see if it matches
    the second parameter"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True  # return true if they find the occurences
        index += 1
    return False  # return false if they didn't find the occurences


def emojified(user_guess: str, secret_word: str) -> str:
    """compare two strings of equal length - return a string composed of emojis"""
    assert len(user_guess) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    index: int = 0
    emoji: str = ""

    while index < len(user_guess):
        if user_guess[index] == secret_word[index]:
            emoji += GREEN_BOX  # correct letter in correct position
        elif contains_char(secret_word=secret_word, char_guess=user_guess[index]):
            emoji += YELLOW_BOX  # correct letter in wrong position
        else:
            emoji += WHITE_BOX  # wrong letter
        index += 1
    return emoji


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # checking turns
    won: bool = False  # flag to exit when user_guess is equal to secret word
    while turn <= len(secret) and not won:
        print(f"=== Turn {turn}/6 ===")
        user_guess = input_guess(lenword=len(secret))
        print(emojified(user_guess, secret))
        if user_guess == secret:
            won = True
        else:
            turn += 1  # add turns until it reaches 6 times

    """print either you won or try agian"""
    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
