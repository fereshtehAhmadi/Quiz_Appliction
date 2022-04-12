from users import get_users
from validate_email import validate_email
from password_validator import PasswordValidator
import re
import termcolor2


def validate_username(username):
    users = get_users()
    user = users.get(username)
    pattern = r"[A-Za-z]+[A-Za-z0-9.-]\S"
    if user:
        print(termcolor2.colored("Username is duplicate!! ", color="red"))
    elif re.fullmatch(pattern, username):
        return True

    print(termcolor2.colored('A username can contain lowercase and upper case letters, numbers and special characters (_ - .).', color="red"))


def validate_password(password):
    
    pattern = PasswordValidator().has().uppercase().has().lowercase().has().digits().has().no().spaces().min(8)
    if bool(pattern.validate(password)):
        return True
    print(termcolor2.colored('A password must contain both lowercase and uppercase letters, numbers and special characters.', color="red"))


def validate_emaill(email):
    if validate_email(email):
        return True
    print(termcolor2.colored('Invalid email.', color="red"))


def validate_city(city):
    pattern = "^[a-z]+$"
    if bool(re.fullmatch(pattern, city)):
        return True
    print(termcolor2.colored('A city contains only strings.', color="red"))


def match_password(password, confirm_password):
    if confirm_password == password:
        return True
    print(termcolor2.colored('Passwords does not match.', color="red"))