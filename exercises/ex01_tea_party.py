"""My first exercise in COMP110!"""

__author__ = "730813516"

"""A function to compute the number of tea bags needed based on number of guests
A function to compute the number of treats needed based on the number of teas guests are expecting to drink
A function to compute the cost of the tea bags and the treats combined
Bringing these function together in a “main planner” function that calls each and produces printed output
Making the program runnable and asking a user for input when they run the program"""


def main_planner(guests: int) -> None:
    """all function"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    """comma for concatenating number and string , plus sign for string concatenation"""
    """if using int for Cost: $, they make space between dollar sign and the number: Convert to string!!"""


def tea_bags(people: int) -> int:
    """the number of guests attending the tea party"""
    return people * 2


def treats(people: int) -> int:
    """the number of guests attending the tea party"""
    return int(tea_bags(people=people) * 1.5)
    """ people in this function is different varible from people in tea_bags function"""


def cost(tea_count: int, treat_count: int) -> float:
    """the total cost of the tea bags and treats combined."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
