from http import HTTPStatus
from sqlalchemy import select, insert, update, delete
from fastapi.responses import Response, ORJSONResponse

from models import get_session
from models.user import User

from .router import user_router
from .dto.user_dto import UserDTO
from .dto.users_dto import UsersDTO
from .dto.add_user_dto import AddUserDTO
from .dto.update_user_dto import UpdateUserDTO

prefix = "/users"
user_prefix = "/users/{user_id}"


@user_router.get(prefix, response_model=UsersDTO)
async def get_all_users() -> UsersDTO:
    async with get_session() as session:
        execution_result = await session.execute(select(User))
        users = [
            UserDTO(username=user.username, full_name=user.full_name)
            for user in execution_result.scalars().all()
        ]

        return UsersDTO(users=users)


@user_router.post(prefix)
async def add_user(user_data: AddUserDTO) -> Response:
    status_code: HTTPStatus = HTTPStatus.NO_CONTENT

    async with get_session() as session:
        get_statement = select(User).where(User.user_id == user_data.user_id)
        user = (await session.execute(get_statement)).scalar()

        if not user:
            add_statement = insert(User).values(
                user_id=user_data.user_id,
                full_name=user_data.full_name,
                username=user_data.username,
            )

            await session.execute(add_statement)
            await session.commit()
            status_code = HTTPStatus.CREATED

        return Response(status_code=status_code)


@user_router.put(user_prefix, status_code=HTTPStatus.NO_CONTENT)
async def update_user(user_id: int, user_data: UpdateUserDTO) -> None:
    async with get_session() as session:
        update_statement = (
            update(User)
            .where(User.user_id == user_id)
            .values(full_name=user_data.full_name, username=user_data.username)
        )

        await session.execute(update_statement)
        await session.commit()


@user_router.delete(user_prefix, status_code=HTTPStatus.NO_CONTENT)
async def remove_user(user_id: int) -> None:
    async with get_session() as session:
        delete_statement = delete(User).where(User.user_id == user_id)

        await session.execute(delete_statement)
        await session.commit()
