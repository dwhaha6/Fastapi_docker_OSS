from fastapi import APIRouter
from model import Todo
import math
todo_router = APIRouter()
todo_list = []
grade_score = {
    "A+": 4.5,
    "A0" : 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
@todo_router.post("/score")
async def add_todo(todo: Todo) -> dict:
    total_credit = 0
    total_score = 0.0
    for i in todo.courses:
        total_credit += i.credits
        sc = i.grade
        total_score += (i.credits * grade_score.get(sc,0.0))
    if total_credit != 0:
        gpa = total_score / total_credit
    else:
        gpa=0.0
    gpa = math.ceil(gpa*100) / 100
    return {
        
        "student_summary": {
            "student_id": todo.student_id,
            "name": todo.name,
            "gpa": gpa,
            "total_credits": total_credit
            }    
        
    }
