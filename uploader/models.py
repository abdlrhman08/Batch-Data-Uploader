from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class OWAccount(Base):

    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[int] = mapped_column(nullable=False)
    
    email: Mapped[str] = mapped_column(String(255), primary_key=True, nullable=False)
    email_password: Mapped[str] = mapped_column(String(40), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    user: Mapped[str] = mapped_column(String(255), nullable=True)

    name: Mapped[str] = mapped_column(String(40), nullable=True)

    battle_tag: Mapped[str] = mapped_column(String(20), nullable=True)
    
    phonenum: Mapped[str] = mapped_column(String(15), nullable=True) 

    safe_um_user: Mapped[str] = mapped_column(String(30), nullable=True)
    safe_um_pass: Mapped[str] = mapped_column(String(30), nullable=True)

    creation_date: Mapped[str] = mapped_column(String(12), nullable=True)
    birthdate: Mapped[str] = mapped_column(String(12), nullable=True)

    finished_date: Mapped[str] = mapped_column(String(12), nullable=True)

    description: Mapped[str] = mapped_column(String(255), nullable=True)

    channelid: Mapped[str] = mapped_column(String(255), nullable=True)

    finished: Mapped[bool] = mapped_column(default=False)
    taken: Mapped[bool] = mapped_column(default=False)
