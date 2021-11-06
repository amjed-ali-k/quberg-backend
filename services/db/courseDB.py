
from models.course import CourseDB, IndividualCourses
from deta import Deta
from config import settings
from typing import List, Optional


deta = Deta(settings.DETA_BASE_KEY)  # configure your Deta project
registration_db = deta.Base('registrations')
courses_db = deta.Base('courses')


async def create_new_registration_in_db(course: CourseDB) -> Optional[CourseDB]:
    coursedb = registration_db.insert(course.dict())
    try:
        return CourseDB(**coursedb)
    except:
        return None


async def get_course_by_id(course_id: str) -> Optional[IndividualCourses]:
    try:
        course = courses_db.get(course_id)
        return IndividualCourses(**course)
    except:
        return None

async def get_all_courses() -> list:
    courses = courses_db.fetch()
    return [IndividualCourses(**course) for course in courses.items]


async def get_all_registrations() -> List[CourseDB]:
    registrations = registration_db.fetch()
    return [CourseDB(**registration) for registration in registrations.items]