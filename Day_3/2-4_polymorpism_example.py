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
    def __init__(self, sound_system):
        print('This car is a BMW.')
        self.sound_system = sound_system
        super().__init__('M300', 'Blue', 'Internal Combustion')

    # an instance method can override it base class version.
    def start(self):
        return print("Growl!")

    # an instance method can extend a base class also.
    def getLuxExperience(self):
        return print(f"Being cool listening to music from my {self.sound_system} in my {self.color} {self.model}")


lux1 = Bmw("Senheizer")

lux1.start()
lux1.talk("Harry")
lux1.getLuxExperience()
