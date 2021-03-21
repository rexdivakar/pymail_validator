import re
import requests


def __email_classification(email):
    if re.findall(r"\S+@+gmail+", email):
        return 'gmail'
    elif re.findall(r"\S+@+hotmail+", email):
        return 'hotmail'
    elif re.findall(r"\S+@+ymail+", email):
        return 'ymail'


def is_valid(email):
    op = __email_classification(email)
    if op == 'gmail':
        try:
            url = "https://mail.google.com/mail/gxlu?email={0}".format(email)
            r = requests.get(url)
            head_value = r.headers['set-cookie']
            return True
        except ConnectionRefusedError as cr:
            return 'Connection Refused Error'
        except KeyError as ke:
            return False


