from pydantic import BaseModel, EmailStr

class User(BaseModel):
    firstName: str
    lastName: str
    username: str
    email: EmailStr
    location: str
    grade: str
    birthday: str
    password: str
    level: int
    gems: int
    victories: int
    dominationRate: int
    rank: int
    killStreak: int
    profileIcon: str
    joinDate: str


class UserOut(BaseModel):
    email: EmailStr
    id: str

class Token(BaseModel):
    access_token: str
    token_type: str