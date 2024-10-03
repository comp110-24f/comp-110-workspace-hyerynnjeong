"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730813516"


def input_word() -> str:
    """input word and check if it contains 5 characters; if not, exit"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # exit when the error occurs
    return word


def input_letter() -> str:
    """input letter and check if it contains single character; if not, exit"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # exit when the error occurs
    return letter


def contains_char(word: str, letter: str) -> None:
    """searching the input letter in the input word;
    inform which index of the word contains letter"""

    count: int = 0  # count how many input letters are in input word
    print("Searching for " + letter + " in " + word)

    """ using ifs to check each index of the word; 
    not elif since we have to go over all the indices"""
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    """ three different output based on the number of count"""
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # s for plural


def main() -> None:
    """main function that runs contains_char function which automatically runs
    both input_word and input_letter functions"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
