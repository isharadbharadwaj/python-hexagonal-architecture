from dependency_injector import containers, providers
from src.infra.postgres_repo import PostgresUserRepository
from src.core.services import UserService
import os
from dotenv import load_dotenv

# FIX: Load .env immediately when this file is imported
load_dotenv()


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.main"])

    config = providers.Configuration()

    # Singleton: We only want ONE database connection pool
    user_repository = providers.Singleton(
        PostgresUserRepository,
        # Now this will correctly find the string instead of None
        db_url=os.getenv("DATABASE_URL")
    )

    # Factory: We want a NEW service instance for every request
    user_service = providers.Factory(
        UserService,
        user_repo=user_repository
    )