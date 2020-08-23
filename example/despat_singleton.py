class Borg:
    """ Borg class making class attributes global """

    _shared_state = dict()      # attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):          # inherits from Borg class
    """ This class now shores all its attributes among its various instances """
    """ This makes the singleton objects an OO global variable               """

    def __init__(self, **kwargs):
        Borg.__init__(self)

        # update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(**kwargs)

    def __str__(self):
        # return the attribute dictionary for printing
        return str(self._shared_state)

# let's create a singleton object and add our first acronym
x = Singleton(http = "hyper text transfer protocal")
print(x)

# let's create another singleton object and see if it refers to the same attribute dictionary
x = Singleton(snmp = "simple network management protocal")
print(x)