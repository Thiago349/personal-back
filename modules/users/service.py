from modules.users.repository import UsersRepository
from modules.users.mapper import UsersMapper
import random

from werkzeug.exceptions import Unauthorized

class UsersService:
    def validate(id: int, password: int):
        user = UsersRepository.validate(id, password)
        userDTO = UsersMapper.entityToDTO(user)

        if user is None:
            raise Unauthorized(f"Wrong Credentials")

        return userDTO
    

    def create(name: str, branch: str):
        password = random.randrange(1000, 10000)
        user = UsersRepository.create(name, password, branch)
        userDTO = UsersMapper.entityToDTO(user)
        return userDTO