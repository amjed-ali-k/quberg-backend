from typing import Optional
from pydantic import BaseModel


class CourseIn(BaseModel):
    fullname: str
    email: str
    phonenumber: str
    id: str


class CourseDB(CourseIn):
    key: str
    time: str


class IndividualCourses(BaseModel):
    id: str
    title: str
    date: Optional[str]
    amount: Optional[str]
    type: str