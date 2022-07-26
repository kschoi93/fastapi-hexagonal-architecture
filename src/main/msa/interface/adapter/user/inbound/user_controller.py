from fastapi import APIRouter

from src.main.msa.interface.port.user.inbound.user_in_port import UserInPort
from src.main.msa.application.service.user.user_service import UserService
from src.main.msa.interface.adapter.user.outbound.user_persistence_adapter import UserPersistenceAdapter

router = APIRouter(prefix='/user')

user: UserInPort = UserService(UserPersistenceAdapter)


@router.post('/sign')
def sign_in() -> None:
    return user.sign_in(email='kschoi@gmail.com', password='12345')