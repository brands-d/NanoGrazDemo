class Car:
    """
    A class representing a car.

    Attributes:

        model (str): The model name of the car.
    """

    count: int = 0

    def __init__(self, model: str = ""):
        self.model = model
        Car.count += 1

    def drive(self, speed: float):
        """
        Drives the car at the specified speed.

        Args:
            speed (float): The speed at which to drive the car, in kilometers per hour (km/h).
        """
        pass

    def __del__(self):
        Car.count -= 1


class Truck(Car):
    """
    Represents a truck, which is a type of car with additional cargo capacity.

    Attributes:
        capacity (int): The cargo capacity of the truck.
    """

    def __init__(self, capacity: int, model: str = ""):
        super().__init__(model)
        self.capacity = capacity
