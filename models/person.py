import sqlite3
from typing import Any, Optional
import sys 
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/:C/Users/thoma/OneDrive/Documents/python-flask/db/db.py')))
from db.db import get_db


class Person:
    def __init__(self, id: Optional[int], name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Person(id={self.id}, name={self.name}, age={self.age})>"

    @classmethod
    def create(cls, name: str, age: int) -> 'Person':
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        person_id = cursor.lastrowid
        conn.close()
        return cls(id=person_id, name=name, age=age)

    @classmethod
    def get_by_name(cls, name: str) -> Optional['Person']:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM people WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row['id'], name=row['name'], age=row['age'])
        return None

if __name__ == "__main__":
    p: Person = Person.create(name="Thomas", age=10)
    thomas: Any = Person.get_by_name("Thomas")
    if thomas:
        print(thomas.name)
    else:
        print("Person not found")
