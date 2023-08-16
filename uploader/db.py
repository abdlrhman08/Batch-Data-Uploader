from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

import pandas as pd
import click

from .models import OWAccount

class db():

    def __init__(self, user: str, passw: str, host: str, database: str) -> None:
        self.url = f"postgresql://{user}:{passw}@{host}/{database}"

    def start_conn(self) -> None:
        '''Create a connection and session makker'''

        self.engine = create_engine(self.url, echo=False)
        self.session = sessionmaker(self.engine, expire_on_commit=False)

    def bulk_upload(self, dataframe: pd.DataFrame) ->  None:
        with self.session() as session:
            
            accs = []
            for index, row in dataframe.iterrows():
                accs.append(OWAccount(
                    type = row["type"],
                    
                    email = row["email"],
                    email_password = row["email_pass"],
                    password = row["password"],
                    name = row["name"],

                    battle_tag = row["battle_tag"],
                    
                    phonenum = str(row["number"]),

                    safe_um_user = str(row["safe_um_user"]),
                    safe_um_pass = row["safe_um_pass"],

                    creation_date = row["creation_date"],
                    birthdate = row["birthdate"],

                    finished = False,
                    taken = False

                ))
                click.echo(f"Found Account: {row['email']}, Accounts found: {index + 1}")
            
            session.add_all(accs)
            session.commit()
        
        click.echo("Uploaded succesfully")
        return accs
