from services.course import store_course_registration
from models.course import CourseDB, CourseIn
from fastapi import Depends, HTTPException, APIRouter
from starlette import status

r = APIRouter()

r.post("/register-course",  tags=['Courses'], response_model=CourseDB)


async def registerCourse(form: CourseIn):
    data = await store_course_registration(form)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="An error occured",
        )
    return data
