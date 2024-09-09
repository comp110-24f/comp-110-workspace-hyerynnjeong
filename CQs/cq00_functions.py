"""CQ00"""

__author__ = "730813516"


def mimic(message: str) -> str:
    """take your input and repeat it back to you!"""
    return message


def main() -> None:
    """print the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
