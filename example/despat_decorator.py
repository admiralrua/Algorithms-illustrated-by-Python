from functools import wraps

def make_blink(function):
    """ define the decorator """

    # this makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    # define the inner function
    def decorator():
        # grab the return value of the function being decoratored
        ret = function()

        # add new functionality to the function being decorated
        return "<blink> " + ret + " </blink>"

    return decorator


# apply the decorator here
@make_blink
def hello_world_dec():
    """ original function """

    return "Hello, World!"


def hello_world():
    """ original function """

    return "Hello, World!"


# check the result of decorating
print(hello_world())
print(hello_world_dec())


# check if the function name and docstring are still the same as those of the function being decorater
print(hello_world_dec.__name__)
print(hello_world_dec.__doc__)