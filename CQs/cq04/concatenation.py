__author__ = "730813516"


def concat(first_word: str, second_word: str) -> str:
    # return the concatenation of the two input strings.
    return first_word + second_word


word1: str = "happy"
word2: str = "tuesday"

print(concat(word1, word2))

if __name__ == "__main__":
    print(concat("happy", "monday"))
