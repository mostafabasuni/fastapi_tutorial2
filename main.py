from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Student(BaseModel):
    id : int
    name: str    
    grade: int
    
students = [
    Student(id=1, name="karim ali", grade=10),
    Student(id=2, name="mostafa basuni", grade=11),    
]


@app.get("/students/")
def get_students():
    return students

@app.post("/students/")
def create_student(New_student: Student):
    students.append(New_student)
    return New_student

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):    
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):    
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted successfully"}
    return {"error": "Student not found"}
