from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy import String ,Integer, Boolean

class Base(DeclarativeBase):
    pass

class OWAccount(Base):

    __tablename__ = "accounts"

    column_definitions = {
        'id': Integer(primary_key=True, autoincrement=True),
        'type': Integer(nullable=False),
        'email': String(255, primary_key=True, nullable=False),
        'email_password': String(40, nullable=False),
        'password': String(255, nullable=False),
        'user': String(255, nullable=True),
        'name': String(40, nullable=True),
        'battle_tag': String(20, nullable=True),
        'phonenum': String(15, nullable=True),
        'safe_um_user': String(30, nullable=True),
        'safe_um_pass': String(30, nullable=True),
        'creation_date': String(12, nullable=True),
        'birthdate': String(12, nullable=True),
        'finished_date': String(12, nullable=True),
        'description': String(255, nullable=True),
        'channelid': String(255, nullable=True),
        'finished': Boolean(default=False),
        'taken': Boolean(default=False),
    }

    for column_name, column_type in column_definitions.items():
        locals()[column_name] = mapped_column(column_type)

    # Constructor for the class
    def __init__(self, **kwargs):
        for column_name, column_type in self.column_definitions.items():
            setattr(self, column_name, kwargs.get(column_name))