from services.db.courseDB import create_new_registration_in_db, get_all_courses, get_course_by_id
from models.course import CourseDB, CourseIn
import uuid
import datetime
from typing import Optional
import aiofiles, json, os


async def store_course_registration(course: CourseIn) -> Optional[CourseDB]:
    print(str(datetime.datetime.timestamp))
    toDB = CourseDB(key=str(uuid.uuid4()),
                    time=datetime.datetime.timestamp(datetime.datetime.now()) * 1000, **course.dict())
    return await create_new_registration_in_db(toDB)


async def get_course(uid: str):
    return await get_course_by_id(uid)


async def get_upcoming_classes():
    return await get_all_courses()
