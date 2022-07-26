from src.main.msa.interface.adapter.user.outbound.user_repository import UserRepository
from src.main.msa.interface.port.user.inbound.user_in_port import UserInPort
from src.main.msa.interface.port.user.outbound.user_out_port import UserOutPort
from src.main.msa.application.domain.user_model import User


class UserService(UserInPort):
    def __init__(self, adapter: UserOutPort) -> None:
        super(UserService, self).__init__(adapter)
        self.adapter = adapter(UserRepository)

    def sign_in(self, email: str, password: str) -> User:
        return self.adapter.sign_ok()