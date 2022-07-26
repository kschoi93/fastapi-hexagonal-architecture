from abc import ABCMeta, abstractmethod, ABC


class UserInPort(metaclass=ABCMeta):
    def __init__(self, adapter):
        pass

    def sign_in(self, email: str, password: str) -> None:
        pass