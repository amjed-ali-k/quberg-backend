from services.course import store_course_registration, get_upcoming_classes, get_course
from models.course import CourseDB, CourseIn
from fastapi import HTTPException, APIRouter
from starlette import status
from services.email import send_mail
r = APIRouter()
tag = "Courses"


@r.post("/register-course", tags=[tag], response_model=CourseDB)
async def register_course(form: CourseIn):
    data = await store_course_registration(form)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="An error occurred",
        )
    course = await get_course(form.id)
    await send_mail(course=f'{course["title"]} in {course["type"]}', **form.dict())
    return data


@r.get("/upcoming-classes", tags=[tag])
async def upcoming_classes_list():
    return await get_upcoming_classes()
