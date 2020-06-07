This note is a kind of summary note of **Python: Design patterns** given by Jungwoo Ryoo in [LinkedIn Learning](https://www.linkedin.com/learning/python-design-patterns).

# Understanding Design Pattern

## What and Why
- consistency of the code: same problems are solved by same solution with minimal modification of code
  - well-known solutions for recurring problems
    - decreasing a risk of making errors
    - increasing a possibility of detecting erros since many coders will look into the design pattern implemented
  - cost-saving
    - no need to reinvent
    - systematic reuse of ideas or best practices yields lower cost and higher quality
- scaling up or enforcing the usage of design patterns
  - by software architecture: identifying patterns to be used throughtout software in a coherent manner
  - by frameworks: a collection of design patterns
- a safe lock for:
  - completeness: how much the solution meet the requirements and how flexible it is for potential customizaton and extension
  - correctness
  - coupling: to which degree software elements are related, strong coupling means change in one element leads to a significant effort to address change in other elements -> less coupling is desriable
  - cohesion: how independent the software element is -> more cohesion is better
  - simplicity and generality trade-offs
    - generality -> more functionality, too complex
    - simplicity -> an easy learning curve for practitioners
- a repository of Python implementation of design patterns can be found [here](https://github.com/faif/python-patterns)
    

## Important characteristics
- language neutral
- dynamic (evolution)
- incomplete **to promote customization**


## Type of design patterns
- creational design patterns
  - are used to create objects in a systematic way
  - are flexibility, i.e.: create different subtypes of objects from the same calss at runtime
  - OOP: polymorphism
- structural design patterns
  - establish useful relationships between software components in certain configurations
  - to accomplish both functional and nonfunctional requirements
  - different goals yield different structures
  - OOP: inheritance
- behavior design patterns
  - are best practice of objects interaction
  - focus on defining the protocols of interactions
  - OOP: methods and their signatures
  

## Core concepts of Object-oriented programming
- Objects
  - represent entities in both problem and solution domains, i.e. components of software interact with each other inside the software
- Classes
  - are templates to create objects to avoid recreating them each time, e.g. cookie cutter
  - define objects in terms of:
    - attributes: represent properties of an entity, capture the state of the entity
    - methods: represent behaviours of the entity 
- Inheritance
  - establishes a relationship between two classes as **parent** and **child**
  - **child** class
    - *keeps* the attributes and methods of its parents
    - *adds* new attributes and methods of its own
    - *overrides* the existing methods of its parent
- Polymorphism
  - relies on inheritance
  - allows child classes to be instantiated and treated as the same type as its parent
  - enables a parent class to be manifested into any of its child classes (to reveal the true nature of a child object)
  

## A pattern context
- participants
  - are classes involved to form a design pattern
  - plays different roles to accomplish the goal of the design pattern
- quality attributes
  - are nonfunctional requirements such as usability, reliability, performance, modifiability...
  - have a hugh effect on the entire software
  - are typically addressed by architecrual solutions
- forces
  - are various factors of trade-offs to consider when adapting a specific design patterns
  - are manifested in quality attributes
  - if they are not addressed well enough, we may have unintended consequences
- consequences
  - are side effects, i.e. better security but worse performance
  - are chosen by decision makers, try to avoid creating more problems than solving an initial problem when a design pattern is misused
  

## A pattern language to define a design pattern
A pattern language consists of:
- name
  - should capture the gist of a pattern
  - becomes part of a vocabulary during the design process
  - hence, should be meaningful and memorable
- context
  - provides a scenario in which the pattern may be used
  - provides more insight, i.e. when and when not to use the pattern
- problem
  - describes a design challenge that the pattern is addressing
- solution 
  - specifies the pattern in term of its *structure* and *behaviour*
  - structure defines the relationships among elements used in the pattern
  - behaviour defines the interactions between elements
- related patterns
  - provides lists of other patterns which are 
    - used together with the pattern being described
    - are similar but different, the differences should be clearly desribed



# Creational patterns
Popular creational patterns consists of five types:
- factory
- abstract factory
- singleton
- builder
- prototype


## Factory
- encapsulates object creation, i.e. objects specifying in creating other objects
- is useful when the client has: 
  - uncertainties in types of objects eventually used in the system
  - decisions to make rearding what classes to use at runtime
  - scenario: a pet shop originally sells dogs, but in the near future will sells also cats -> objects to handle both dogs and cats, for example how the object speaks ("woof"- vs "meow"-sound), the true nature of the object only reveals in the runtime
- example:
  ```python
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
  ```  
  - this example illustrates the use of the **factory pattern**, with this pattern, it is easy to add more objects
  - the implementation above is not a conventional **factory pattern** implememented in other OOP language since that implementation used some conveniences of Python.
- More information can be found [here](https://refactoring.guru/design-patterns/factory-method/python/example)


## Abstract factory
- is useful when the client:
  - expects to create a family of multiple related objects at a given time
  - but doesnt have to know which family it is until runtime
  - scenario: a pet shop with a dog factory and a cat factory with their corresponding attributes such as foods
  - solution:
    - abstract factory: pet factory
    - concrete factory: dog factory and cat factory
    - abstract product: normally it is an inheritance type classes but since Python is a dynamic-type language and thereforce did not require abstract classes
    - concrete product: dog and dog food, cat and cat food
- example:
    ```python
    class Dog:
        """ One of the objects to be returned """

        def __init__(self, name="default"):
            self._name = name

        def speak(self):
            return "Woof!"

        def __str__(self):
            return "Dog."

    class DogFactory:
        """ Concrete Factory """

        def get_pet(self):
            """ Returns a Dog object """

            return Dog()

        def get_food(self):
            """ Returns a Dog Food object """

            return "Dog Food!"

    class PetStore:
        """ PetStore houses our Abstract Factory """

        def __init__(self, pet_factory=None):
            """ pet_factory is our Abstract Factory """

            self._pet_factory = pet_factory

        def show_pet(self):
            """ Utility method to display the details of the objects return by the DogFactory """

            pet = self._pet_factory.get_pet()
            pet_food = self._pet_factory.get_food()

            print("Our pet is '{}'!".format(pet))
            print("Our pet says hello by '{}'".format(pet.speak()))
            print("Its food is '{}'".format(pet_food))

    # create a Concrete Factory
    factory = DogFactory()

    # create a pet store housing Abstract Factory
    shop = PetStore(factory)

    # invoke the utility method to show the details of our pet
    shop.show_pet()     
    ```
- More information and/or example can be found [here](https://refactoring.guru/design-patterns/abstract-factory/python/example) and [here](https://en.wikipedia.org/wiki/Abstract_factory_pattern).


## Singleton
- reflects the way of providing global variables in OOP
- is only one object instanced from a class
- is used as an information cache and shared by multiple objects/elements of a software
- a popular implementation of the singleton is the Borg design pattern
- example:
  ```python
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
  ```


## Builder


## Prototype
  

# Structural patterns
Popular structural patterns consists of five types:
- decorator
- proxy
- adapter
- composite
- bridge
  

# Behavioural patterns
Popular behavioural patterns consists of five types:
- observer
- visitor
- iterator
- strategy
- chain of responsibility




