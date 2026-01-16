from src.core.interfaces import UserRepository
from src.core.domain import User


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, email: str) -> User:
        if self.user_repo.get_by_email(email):
            raise ValueError(f"User with email {email} already exists.")

        # Business logic: Create new user instance
        new_user = User(id=None, email=email)
        return self.user_repo.save(new_user)