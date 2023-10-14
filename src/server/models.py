from pydantic import BaseModel

class CreateUser(BaseModel):
    user_login: str
    user_password: str
    user_mail: str
    user_phone: str | None = None
    user_name: str
    user_surnames: str
    user_birthdate: str