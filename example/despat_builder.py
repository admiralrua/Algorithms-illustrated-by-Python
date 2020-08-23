class Director():
    """ Director """
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_engine()
        self._builder.add_tires()


    def get_car(self):
        return self._builder.car


class Builder():
    """ Abstract builder """
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """ Concrete builder -> provides parts and tools to work on the parts """
    def add_model(self):
        self.car.model = "SkyLark"

    def add_engine(self):
        self.car.engine = "Turbo engine"

    def add_tires(self):
        self.car.tires = "HighSpeed tires"


class Car():
    """ Product """
    def __init__(self):
        self.model = None
        self.engine = None
        self.tires = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.engine, self.tires)


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)