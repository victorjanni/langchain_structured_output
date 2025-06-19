from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class student(BaseModel):
    name: str = 'victor'
    age: Optional[int] = None
    email:EmailStr
    cgpa: float = Field(gt=0,lt=10, default=5, description="it is the value of grade")

new_student = {'age':27, 'email':'asd@gmail.com'}

student = student(**new_student)

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()