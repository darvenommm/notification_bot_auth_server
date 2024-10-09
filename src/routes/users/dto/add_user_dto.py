from pydantic import BaseModel


class AddUserDTO(BaseModel):
    user_id: int
    username: str
    full_name: str
