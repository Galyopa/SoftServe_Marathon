"""
Create a class Employee that will take a full name as argument,
 as well as a set of none, one or more keywords.

Each instance should have a name and
 a lastname attributes plus one more attribute for each of the keywords, if any.
"""


class Employee:
    def __init__(self, full_name, **kwargs):
        fio = full_name.split(' ')
        self.name = fio[0]
        self.lastname = fio[1]
        self.__dict__.update(kwargs)




john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
print(mary.lastname)
print(richard.height)
print(giancarlo.nationality)
print(john.name)
print(mary.__dict__)
print(Employee.__dict__)
