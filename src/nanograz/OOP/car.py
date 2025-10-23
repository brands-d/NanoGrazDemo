class Car:
    """
    A class representing a car.

    Attributes:

        model (str): The model name of the car.
    """

    count: int = 0

    models_by_brand = {
        "VW": "VW Golf",
        "Toyota": "Toyota Corolla",
        "Ford": "Ford Focus",
    }

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

    @staticmethod
    def mph_to_kmh(speed_mph: float) -> float:
        """Convert a speed from miles per hour (mph) to kilometers per hour (km/h).

        Args:
            speed_mph (float): Speed in miles per hour.

        Returns:
            float: Equivalent speed in kilometers per hour. Conversion uses the factor
            1 mile = 1.60934 kilometers.
        """
        return speed_mph * 1.60934

    @classmethod
    def from_brand(cls, brand: str) -> "Car":
        """
        Creates a Car instance based on the brand name.

        Args:
            brand (str): The brand of the car.

        Returns:
            Car: An instance of Car with a model name corresponding to the brand.
        """
        try:
            model = cls.models_by_brand[brand]
        except KeyError:
            raise ValueError(f"Unknown brand: {brand}")
        else:
            return cls(model=model)

    def __del__(self):
        # defensive: avoid negative counts if destructor called unexpectedly
        if Car.count > 0:
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
