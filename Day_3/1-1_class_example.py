class Car:
    # class attribute
    wheel_count = 4

    # instance attribute
    def __init__(self, model, color, engine_type, driver=None):
        self.model = model
        self.color = color
        self.engine_type = engine_type
        self.driver = driver

    # Instance Methods
    def start(self):
        return print("Vroom!")

    def talk(self, driver):
        return print(f"Hello {driver}!!")


# instantiate the Parrot class
bmw = Car("M300", "Blue", "Hybrid")
tesla = Car("Smod", "Black", "Electric")

# access the class attributes
print("bmw has {} wheels.".format(bmw.__class__.wheel_count))
print("tesla has {} wheels.".format(bmw.__class__.wheel_count))

# access the instance attributes
print("The BMW {} is {}.".format( bmw.model, bmw.color))
print("The Tesla {} is {}.".format( tesla.model, tesla.color))

# Access Instance methods
tesla.start()
tesla.talk("Jim")
