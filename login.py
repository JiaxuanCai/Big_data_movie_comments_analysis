import requests

class DouBan:
    def __init__(self):
        self.login_url = 'https://accounts.douban.com/j/mobile/login/basic'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }
        self.login_data = {
            'ck': '',
            'remember': 'false',
            'name': '13388958463',
            'password': 'cm000610'
        }
        self.session = requests.Session()
        self.get_html(self.login_url)
        self.login()

    def login(self):
        response = self.session.post(self.login_url, data=self.login_data, headers=self.headers)
        print(response.json())

    def get_html(self, url):
        return self.session.get(url, headers = self.headers)