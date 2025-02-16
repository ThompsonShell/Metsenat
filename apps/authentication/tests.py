import requests

class EskizUz:
    def get_token(self):
        url = "https://notify.eskiz.uz/api/auth/login"

        data = {
            "email": "<EMAIL>",
            "password": "<PASSWORD>"
        }

        res = requests.post(url, json=data)
        print(res.status_code, res.json())

