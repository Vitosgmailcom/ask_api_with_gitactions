
import random
import string


def random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = "gmail.com"
    if not email_prefix:
        email_prefix = "testuser_"

    str_lenght = 5
    random_string = "".join(random.choices(string.ascii_lowercase, k=str_lenght))
    random_email = email_prefix + random_string + "@" + domain

    password_lenght = 5
    random_pass = "".join(random.choices(string.ascii_letters, k=password_lenght))

    random_email_password = {
        "email": random_email,
        "password": random_pass
    }
    return random_email_password



