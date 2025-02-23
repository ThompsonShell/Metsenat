from pyexpat.errors import messages

import requests

class EskizUz:

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def get_token(self):
        """ get auth token """

        url = "https://notify.eskiz.uz/api/auth/login"


        data = {
            'email': self.username,
            'password': self.password
        }

        res = requests.post(url, json=data)
        res_data = res.json()
        if res.status_code != 200:
            raise ValueError(res_data["message"])
        return res_data['data']["token"]

eskiz_uz_service = EskizUz(email='<EMAIL>', password='<PASSWORD>')
try:
    eskiz_uz_service.get_token()
except ValueError as e:
    print(e)


