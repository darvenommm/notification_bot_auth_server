from pydantic import BaseModel

from .user_dto import UserDTO


class UsersDTO(BaseModel):
    users: list[UserDTO]
