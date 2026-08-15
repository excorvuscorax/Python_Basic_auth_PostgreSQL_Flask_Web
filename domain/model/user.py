import uuid
from dataclasses import dataclass, field


def generate_user_id():
    return str(uuid.uuid4())


@dataclass
class User:
    user_id: str = field(default_factory=generate_user_id)
    login: str = ""
    password: str = ""
