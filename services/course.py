from services.db.courseDB import create_new_registration_in_db
from models.course import CourseDB, CourseIn


import uuid
import datetime
from typing import Optional


async def store_course_registration(course: CourseIn) -> Optional[CourseDB]:
    toDB = CourseDB(key=uuid.uuid4(),
                    time=datetime.datetime.timestamp(), **course)
    return await create_new_registration_in_db(toDB)
