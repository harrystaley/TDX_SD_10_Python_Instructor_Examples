from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def get_sides(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def get_sides(self):
        print("I have 3 sides")


class Pentagon(Polygon):
    # overriding abstract method
    def get_sides(self):
        print("I have 5 sides")


class Hexagon(Polygon):
    # overriding abstract method
    def get_sides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def get_sides(self):
        print("I have 4 sides")


if __name__ == "__main__":
    # Driver code
    R = Triangle()
    R.get_sides()

    K = Quadrilateral()
    K.get_sides()

    R = Pentagon()
    R.get_sides()

    K = Hexagon()
    K.get_sides()
