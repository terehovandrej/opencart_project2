import allure

from db_client import DbClient


class ProductQueries(DbClient):
    def get_product(self, name):
        with allure.step(f"Получили продукт {name} из БД"):
            self.cursor.execute(
                "SELECT * FROM oc_product_description WHERE name=?", (name,))
            for name in self.cursor:
                return name

    def add_product(self, name, model):
        with allure.step(f"Добавили продукт {name}, {model} в БД"):
            try:
                self.cursor.execute(
                    "INSERT INTO oc_product (product_id, model, sku, upc, ean, jan, isbn, mpn, location, "
                    "stock_status_id, manufacturer_id, tax_class_id, date_added, date_modified) "
                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    ('99', model, '', '', '', '', '', '', '', '6', '0', '0', '2020-07-02 07:39:01', '2020-07-02 07:39:01'))
            except self.connect.Error as e:
                print(f"Error: {e}")
            try:
                self.cursor.execute(
                    "INSERT INTO oc_product_description (product_id, language_id, name, "
                    "description, tag, meta_title, meta_description, meta_keyword) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    ('99', '1', name, '', '', 'metatagiphone', '', ''))
            except self.connect.Error as e:
                print(f"Error: {e}")

    def check_product_deleted(self, name, model):
        with allure.step(f"Проверили в БД что продукт {name}, {model} удален"):
            self.cursor.execute(
                "SELECT * FROM oc_product_description WHERE name=?", (name,))
            for name in self.cursor:
                assert name is None
            self.cursor.execute(
                "SELECT * FROM oc_product WHERE model=?", (model,))
            for model in self.cursor:
                assert model is None
