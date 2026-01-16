from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.interfaces import UserRepository
from src.core.domain import User

Base = declarative_base()

# SQLAlchemy Model (Table Definition)
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

class PostgresUserRepository(UserRepository):
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        # Auto-create tables for demo purposes
        Base.metadata.create_all(bind=self.engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def save(self, user: User) -> User:
        session = self.SessionLocal()
        try:
            db_user = UserModel(email=user.email, is_active=user.is_active)
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
            # Map SQL Model -> Domain Entity
            return User(id=db_user.id, email=db_user.email, is_active=db_user.is_active)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_by_email(self, email: str) -> User | None:
        session = self.SessionLocal()
        try:
            db_user = session.query(UserModel).filter(UserModel.email == email).first()
            if db_user:
                return User(id=db_user.id, email=db_user.email, is_active=db_user.is_active)
            return None
        finally:
            session.close()