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
