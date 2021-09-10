from services.course import store_course_registration
from models.course import CourseDB, CourseIn
from fastapi import HTTPException, APIRouter
from starlette import status
import aiofiles, json, os

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
    return data


@r.get("/upcoming-classes", tags=[tag])
async def upcoming_classes_list():
    async with aiofiles.open(os.getcwd() + '/views/' + 'upcomingClasses.json', mode='r') as f:
        sensors = json.loads(await f.read())
    return sensors
