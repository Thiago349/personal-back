import uuid
from alchemy import db_session
from modules.users.entity import User


class UsersRepository: 
    def validate(id: int, password: int):
        try:
            result = db_session.query(User).filter((User.id == id) & (User.password == password)).first()
            return result
        
        except Exception as e:
            db_session.rollback()
            raise e
        
    
    def create(name: str, password: int, branch: str):
        try:
            user = User(
                name = name,
                password = password,
                branch = branch
            )
            db_session.add(user)
            db_session.flush()
            db_session.commit()
            return user
        
        except Exception as e:
            db_session.rollback()
            raise e