from pydantic import BaseModel


class UserRegistrationValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str
    city: str


class EditUserValidator(BaseModel):
    user_id: int
    edit_info: str
    new_info: str
