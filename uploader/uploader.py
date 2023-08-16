import click
import os
import pandas as pd

from .db import db
from .models import OWAccount
from .utils import info_text

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

@click.group()
@click.pass_context
def cli(ctx: click.Context):
    ctx.obj = db(DB_USER, DB_PASS, DB_HOST, DB_NAME)

@cli.command()
@click.argument("filepath")
@click.option("--gen", type=str)
@click.pass_context
def upload(ctx: click.Context, filepath: str, gen: str):
    '''Used to upload the accounts in the excel sheet to the database'''
    accounts_data = pd.read_excel(filepath)

    #Get a connection to the database and upload
    ctx.obj.start_conn()
    uploaded_accs = ctx.obj.bulk_upload(accounts_data)

    if gen is None:
        return

    #Generate account info
    acc : OWAccount
    filepath = f"{gen}/"

    if gen != "." or gen.endswith("/"):
        filepath = gen
        os.makedirs(os.path.dirname(gen), exist_ok=True)

    for acc in uploaded_accs:
        with open(f"{filepath}{acc.id}.txt", "w") as info_file:
            info_file.write(info_text(acc))

if __name__ == "__main__":
    cli()
