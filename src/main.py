from .utils import *
from .constants import *


def letterify(n: int) -> str:
    """
    Converts a number to its equivalent in words.

    Parameters:
    n (int): The number to be converted.

    Returns:
    str: The word equivalent of the input number.
    """
    if n == 0:
        return "zero"

    letter_num = []

    for i, chunk in enumerate(chop_num(n), start=1):
        if chunk == 0:
            continue
        else:
            letter_num.insert(0, triplets_suffixes[i])

            if chunk < 20:
                letter_num.insert(0, num_2_letter(chunk, ones, teens, tens))
            else:
                for d in expand(chunk):
                    letter_num.insert(0, num_2_letter(d, ones, teens, tens))

    return " ".join(letter_num).strip().capitalize()


if __name__ == "__main__":
    print(letterify(13_356_100_001))


# Example:
# >>> letterify(13_356_100_001)
# 'thirteen billion three hundred fifty six million one hundred thousand one'
