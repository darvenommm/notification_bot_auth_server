from pydantic import BaseModel


class UpdateUserDTO(BaseModel):
    username: str
    full_name: str
