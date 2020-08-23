class Dog:
    """ A simple dog class """

    def __init__(self, name):
        self._name = name

    def speak(self):
        return self._name + ": Woof!"

class Cat:
    """ A simple cat class """

    def __init__(self, name):
        self._name = name

    def speak(self):
        return self._name + ": Meow!"

def get_pet(pet = "dog1"):
    """ The factory method """

    pets = dict(dog1=Dog("Hope"),
                dog2=Dog("Alpha"),
                dog3=Dog("Bravo"),
                cat1=Cat("Peace"),
                cat2=Cat("Cheetah"),
                cat3=Cat("Dennish"))
    return pets[pet]


d = get_pet("dog1")
print(d.speak())

c = get_pet("cat3")
print(c.speak())