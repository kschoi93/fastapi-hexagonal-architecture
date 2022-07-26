from abc import ABCMeta

from src.main.msa.application.domain.user_model import User


class UserOutPort(metaclass=ABCMeta):
    def sign_ok(self) -> User:
        pass