from services.db.courseDB import create_new_registration_in_db
from models.course import CourseDB, CourseIn


import uuid
import datetime
from typing import Optional


async def store_course_registration(course: CourseIn) -> Optional[CourseDB]:
    print(str(datetime.datetime.timestamp))
    toDB = CourseDB(key=str(uuid.uuid4()),
                    time=datetime.datetime.timestamp(datetime.datetime.now())*1000, **course.dict())
    return await create_new_registration_in_db(toDB)
