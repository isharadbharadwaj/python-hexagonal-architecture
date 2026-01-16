from dataclasses import dataclass

@dataclass
class User:
    id: int | None
    email: str
    is_active: bool = True