from services.db.courseDB import create_new_registration_in_db
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
    async with aiofiles.open(os.getcwd() + '/views/' + 'courses.json', mode='r') as f:
        classes = json.loads(await f.read())
    return list(filter(lambda x: x['id'] == uid, classes))[0]


async def get_upcoming_classes():
    async with aiofiles.open(os.getcwd() + '/views/' + 'upcomingClasses.json', mode='r') as f:
        classes = json.loads(await f.read())
    return classes
