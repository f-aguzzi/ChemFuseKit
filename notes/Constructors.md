#python

The basic syntax for a Python constructor is the following:

```python
class Person:
	def __init__(self, name):
		self.name = name
```

The constructor always takes the name of `__init()__`. The first parameter of the constructor is always a self-reference and is conventionally named self but it could take any other name.

The constructor from the previous example can be instantiated this way:

```python
person = Person("Bob")
```

In the case of a [[Subclass|subclass]], we can invoke the superclass constructor this way:

```python
class Employee(Person):
	def __init__(self, name, employee_id):
		super().__init__(name)
		self.employee_id = employee_id
```

Constructors can be overloaded in the sense that some of their parameters can be made optional by providing them with a default value: This piece of code, for example, will initialize a bank account with no owner and a balance of 0€:

```python
class BankAccount:
	def __init__(self, owner=None, balance=0):
		self.owner = owner
		self.balance = balance

account = BankAccount()
```
