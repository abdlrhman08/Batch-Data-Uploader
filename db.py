from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

from models import OWAccount

class db():

    def __init__(self, user: str, passw: str, host: str, database: str) -> None:
        self.url = f"postgresql://{user}:{passw}@{host}/{database}"

    def start_conn(self) -> None:
        '''Create a connection and session makker'''

        self.engine = create_engine(self.url, echo=True)
        self.session = sessionmaker(self.engine, expire_on_commit=False)

    def upload_acc(self, **kwargs) ->  None:
        with self.session() as session:
            statement = insert(OWAccount).values(
                type = kwargs.get("type"), 
                email = kwargs.get("email"),
                email_password = kwargs.get("email_password"),
                password = kwargs.get("password"),
                name = kwargs.get("name"),
                battle_tag = kwargs.get("battle_tag"),
                phonenum = kwargs.get("phonenum"),
                safe_um_user = kwargs.get("safeum_usr"),
                safe_um_pass = kwargs.get("safeum_pass"),
                finished = False,
                taken = False    
            )
            session.execute(statement)
            session.commit()
