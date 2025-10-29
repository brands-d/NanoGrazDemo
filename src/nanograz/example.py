from re import compile, findall


def square(x: int | float) -> int | float:
    """
    Calculates the square of a number.

    Args:
        x (int|float): The number to be squared.

    Returns:
        int|float: The square of the input number.
    """
    return x * x


def foo(x: int, y: str = "foo"):
    """
    Demo function to demonstrate type annotations.

    Args:
        x (int): An integer input.
        y (str, optional): A string input. Defaults to "foo".

    Returns:
        int
    """

    z: int = x * len(y)
    return z


def custom_match(text: str, regex: str) -> list[str]:
    """
    Custom regex match function that finds all occurrences of a pattern in the given text.

    Args:
        text (str): The text to search within.
        pattern (str): The regex pattern to search for.

    Returns:
        list[str]: A list of all matches found in the text.
    """
    pattern = compile(regex)
    matches = findall(pattern, text)

    return matches
