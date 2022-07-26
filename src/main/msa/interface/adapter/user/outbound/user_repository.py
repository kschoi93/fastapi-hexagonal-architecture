# from ....database import

from src.main.msa.interface.adapter.user.outbound.user_entity import UserEntity


class UserRepository:
    def find_by_user(self) -> UserEntity:
        user = UserEntity(**{'username': 'test'})
        return user