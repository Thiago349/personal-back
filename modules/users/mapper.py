from modules.users.entity import User


class UsersMapper:
    def entityToDTO(user: User):
        userDTO = {
            'id': user.id,
            'password': user.password,
            'name': user.name,
            'branch': user.branch
        }
            
        return userDTO
