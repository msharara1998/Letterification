

def expand(n: int) -> list[int]:
    """
    Breaks down a number into its constituent parts in terms of tens, hundreds, etc.

    Parameters:
    n (int): The number to be expanded.

    Returns:
    List[int]: A list of integers representing the constituent parts of the input number.
    """
    vals = list()
    i = 1
    while n > 0:
        d_val = n % 10
        if d_val:
            vals.append(d_val * i)
        n = n // 10
        i *= 10
    return vals


def chop_num(n: int) -> list[int]:
    """
    Breaks down a number into chunks of three digits each, starting from the right.

    Parameters:
    n (int): The number to be chopped.

    Returns:
    List[int]: A list of integers representing the chunks of the input number.
    """
    l = list()
    t = ""
    c = 0
    for i in str(n)[::-1]:
        t = i + t
        c += 1
        if not c % 3:
            l.append(int(t))
            t = ""
    l.append(int(t)) if t else None
    return l


def num_2_letter(
    n: int,
    ones: dict[int, str],
    teens: dict[int, str],
    tens: dict[int, str]
) -> str | None:
    """
    Converts a number to its equivalent in words.

    Parameters:
    n (int): The number to be converted.
    ones (Dict[int, str]): A dictionary mapping single digit numbers to their equivalent in words.
    teens (Dict[int, str]): A dictionary mapping teen numbers to their equivalent in words.
    tens (Dict[int, str]): A dictionary mapping tens numbers to their equivalent in words.

    Returns:
    Union[str, None]: The word equivalent of the input number, or None if the number is not handled.
    """
    match n:
        case n if n < 10:
            return ones[n]
        case n if n < 20:
            return teens[n]
        case n if n < 100:
            return tens[n]
        case n if n < 1_000:
            return ones[n / 100] + " hundred"