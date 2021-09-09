
from models.course import CourseDB
from deta import Deta
from config import settings
from typing import Optional


deta = Deta(settings.DETA_BASE_KEY)  # configure your Deta project
courses_db = deta.Base('registrations')


async def create_new_registration_in_db(course: CourseDB) -> Optional[CourseDB]:
    coursedb = courses_db.insert(course.dict())
    try:
        return CourseDB(**coursedb)
    except:
        return None
