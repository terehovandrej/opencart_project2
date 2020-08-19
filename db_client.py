import mariadb


class DbClient:
    def __init__(self):
        self.connect = mariadb.connect(
            user="bn_opencart",
            password="",
            host="127.0.0.1",
            port=3306,
            database="bitnami_opencart"
        )
        self.cursor = self.connect.cursor()
