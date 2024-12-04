class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Person(id={self.id}, name={self.name}, age={self.age})>"
