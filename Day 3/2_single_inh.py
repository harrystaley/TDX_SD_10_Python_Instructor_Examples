class Car:
    # class attribute - Inherited by all instances of a class.
    wheel_count = 4

    # instance attribute - specific data about an instance.
    def __init__(self, model, color, engine_type, driver=None):
        self.model = model
        self.color = color
        self.engine_type = engine_type
        self.driver = driver

    # Instance Methods - methods specific to an instance
    def start(self):
        return print("Vroom!")

    def talk(self, driver):
        return print(f"Hello {driver}!!")


class Bmw(Car):
    def __init__(self):
        print('This car is a BMW.')
        super().__init__('M300', 'Blue', 'Internal Combustion')


MX113 = Bmw()
print(type(MX113))
MX113.start()
MX113.talk("Harry")