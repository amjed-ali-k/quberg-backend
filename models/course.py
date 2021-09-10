from pydantic import BaseModel


class CourseIn(BaseModel):
    fullname: str
    email: str
    phonenumber: str
    id: str


class CourseDB(CourseIn):
    key: str
    time: str
