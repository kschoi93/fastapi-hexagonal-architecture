from src.main.msa.interface.adapter.user.outbound.user_entity import UserEntity
from src.main.msa.interface.adapter.user.outbound.user_repository import UserRepository
from src.main.msa.interface.port.user.outbound.user_out_port import UserOutPort


class UserPersistenceAdapter(UserOutPort):
    def __init__(self, repository: UserRepository):
        super(UserPersistenceAdapter, self).__init__()
        self.repository: UserRepository = repository()

    def sign_ok(self) -> UserEntity:
        return self.repository.find_by_user()