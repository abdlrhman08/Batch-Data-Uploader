from .models import OWAccount

def info_text(account: OWAccount):
    type: str
    name = account.name.split()

    if (account.type == 0):
        type = "50 Wins"
    else:
        type = str(account.type) + " Role"

    return f"""Created: {account.creation_date}

Recovery mail: {account.email}
Password: {account.email_password}

Battle Tag: {account.battle_tag}
Password: {account.password}

Account Type: {type}

Country: Latvia
Phone: {account.phonenum}
Birthdate: {account.birthdate}

First Name: {name[0]}
Last Name: {name[1]}

SafeUM User: {account.safe_um_user}
SafeUM Pass: {account.safe_um_pass}

Description: {account.description}"""
    