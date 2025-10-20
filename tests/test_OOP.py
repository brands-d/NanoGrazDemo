import pytest

from nanograz.OOP.car import Car, Truck
from nanograz.OOP.vector import Vector


@pytest.fixture
def car():
    return Car(model="VW Golf")


@pytest.fixture
def car2():
    return Car()


@pytest.fixture
def truck():
    return Truck(capacity=1000)


def test_classes_vs_objects(car, car2):
    # Classes are not objects
    assert Car != car
    # Two objects of the same class are not the same
    assert car2 != car
    # But they are instances of the same class
    assert car2.__class__ == car.__class__


def test_polymorphism(car, truck):
    # Car object is an instance of Car but not Truck
    assert isinstance(car, Car)
    assert not isinstance(car, Truck)

    # Truck object is an instance of both Truck and Car -> Polymorphism
    assert isinstance(truck, Truck)
    assert isinstance(truck, Car)


def test_class_attributes():
    assert Car.count == 0
    truck = Truck(1000)
    assert Car.count == 1
    assert Truck.count == Car.count
    del truck
    assert Car.count == 0


def test_car(car):
    assert car.model == "VW Golf"


@pytest.fixture
def a():
    return Vector(1, 2)


@pytest.fixture
def b():
    return Vector(3, 4)


def test_vector_addition(a, b):
    c = a + b

    assert repr(c) == "2D-Vector: (4, 6)"
