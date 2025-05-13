class Person:
    name="anonymous"
    @classmethod
    def changeName(cls,name):
        cls.py=name

p1=Person()
p2=Person()
p1.changeName("xxx")
print(p1.name)
print(Person.name)
print(p2.py)
print(p2.py)
print(p2.py)
