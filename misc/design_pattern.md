This note is a kind of summary note of **Python: Design patterns" given by Jungwoo Ryoo in [LinkedIn Learning](https://www.linkedin.com/learning/python-design-patterns).

# Understanding Design Pattern

## What and Why
- Well-known solutions for recurring problems
- no need to reinvent
- systematic reuse of ideas or best practices yields lower cost and higher quality


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
  - child class
    - **keeps** the attributes and methods of its parents
    - **adds** new attributes and methods of its own
    - **overrides** the existing methods of its parent
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
  
  
  
  
  
