from pydantic import BaseModel


class UserDTO(BaseModel):
    username: str
    full_name: str
