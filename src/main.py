from typing import Literal

from .constants import *
from .utils import *


def letterify(
    n: int,
    lang: Literal["en", "ar"] = "en"
) -> str:
    """
    Converts a number to its equivalent in words.

    Parameters:
    n (int): The number to be converted.

    Returns:
    str: The word equivalent of the input number.
    """
    if n == 0:
        return "zero" if lang == "en" else "صفر"

    letter_num = []

    for i, chunk in enumerate(chopped_numbers:= chop_num(n), start=1):

        if chunk == 0:
            continue
        else:
            if lang == "ar" and i != 1:
                letter_num.insert(0, "و")
            letter_num.insert(0, triplets_suffixes[lang][i])

            if chunk < 20:
                letter_num.insert(0, num_2_letter(chunk, lang))
            else:
                expanded_chunk = expand(chunk)
                # Handle Arabic special case for tens and ones order
                if len(expanded_chunk) >= 2 and lang == "ar":
                    expanded_chunk[0], expanded_chunk[1] = expanded_chunk[1], expanded_chunk[0]

                for d in expanded_chunk:
                    if lang == "ar" and expanded_chunk.index(d) != 0:
                        letter_num.insert(0, "و")
                    letter_num.insert(0, num_2_letter(d, lang))

    joining_char = " " if lang == "en" else " "
    return joining_char.join(letter_num).strip().capitalize()


if __name__ == "__main__":
    print(letterify(13_356_100_001, "ar"))
    print(letterify(1_300_010, "ar"))
# 
# Example:
# >>> letterify(13_356_100_001)
# 'thirteen billion three hundred fifty six million one hundred thousand one'
# >>> letterify_ar(13_356_100_001)
# 'ثلاثة عشر مليار ثلاثمئة خمسون ستة مليون مئة ألف واحد'
# ثلاثة عشر مليار ثلاثمئة خمسون ستة مليون مئة ألف واحد

ثلاثة عشر مليار و ثلاثمئة و ستة و خمسون مليون و مئة ألف و واحد