# Week 2 Lab 3: pdb practice.
# This program has a bug caused by a value being the wrong type.


def add_bonus(score):
    """Return score after adding a five-point bonus."""
    return score + 5


def main():
    score = input("Enter score: ")
    breakpoint()
    final_score = add_bonus(score)
    print("Final score:", final_score)


if __name__ == "__main__":
    main()
