import copy

class Prototype:
    """ A factory to store different prototypes """

    def __init__(self):
        """ create a dictionary object containing objects that will be cloned """
        self._objects = dict()

    def register_object(self, name, obj):
        """ register an object to be cloned """
        self._objects[name] = obj

    def unregister_object(self, name):
        """ unregister an object """
        del self._objects[name]

    def clone(self, name):
        """ clone a registered object and update its attributes """
        obj = copy.deepcopy(self._objects.get(name))
        return obj


class Product:
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


class Car(Product):
    def __init__(self, name, color, option):
        self.name = name
        self.color = color
        self.options = option


# create a prototypical instance
skylark = Car(name = 'SkyLark', color = 'Black', option = 'Ex')
tesla   = Car(name = 'Tesla', color = 'Matt Black', option = 'Lux')
toyota  = Car(name = 'Toyota', color = 'Bluish Black', option = 'Nor')

# registering
prototype = Prototype()
prototype.register_object('SkyLark',skylark)
prototype.register_object('Tesla',tesla)
prototype.register_object('Toyota',toyota)

# cloning
c1 = prototype.clone(name = 'SkyLark')
print(c1)
c2 = prototype.clone(name = 'Tesla')
print(c2)
c3 = prototype.clone(name = 'Toyota')
print(c3)