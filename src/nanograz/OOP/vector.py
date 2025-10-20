import logging
from pathlib import Path
from platformdirs import user_log_dir

log_path = Path(user_log_dir("nanograz", "Dominik Brandstetter"))
log_path.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=log_path / "nanograz.log", level=logging.INFO)
logger = logging.getLogger(__name__)


class Vector:
    """
    Represents a 2-dimensional vector with x and y components.

    Args:
        x (float): The x component of the vector.
        y (float): The y component of the vector.

    Attributes:
        x (float): The x component of the vector.
        y (float): The y component of the vector.

    Methods:
        __add__(other):
            Adds this vector to another vector.

        __repr__():
            Returns a string representation of the vector.
    """

    def __init__(self, x: float, y: float):
        logger.info(f"Creating Vector with x={x}, y={y}")
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        """
        Adds two Vector instances component-wise.

        Args:
            other (Vector): The vector to add to this vector.

        Returns:
            Vector: A new vector representing the sum of this vector and `other`.
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        """
        Return a string representation of the 2D vector in the format '2D-Vector: (x, y)'.

        Returns:
            str: A string showing the x and y components of the vector.
        """
        return f"2D-Vector: ({self.x}, {self.y})"
