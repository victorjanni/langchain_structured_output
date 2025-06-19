from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name':'victor', 'age':27}

print(new_person)