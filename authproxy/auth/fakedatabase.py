from flask_login import UserMixin
from passlib.context import CryptContext

from ..settings import username, password, session_token, api_key

pwd_context = CryptContext(schemes=['sha512_crypt'])


class User(UserMixin):

    username = username
    password = password
    session_token = session_token
    apikey = api_key

    def verify_password(self, password):
        if self.password is None:
            return False
        valid, _ = pwd_context.verify_and_update(password,
                                                 self.password)
        return valid

    def get_id(self):
        return self.session_token
