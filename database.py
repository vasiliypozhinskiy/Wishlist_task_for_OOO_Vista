import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing


class Database:
    def __init__(self):
        self.options = {'host': 'localhost',
                        'user': 'wishlist',
                        'password': '123qweASD',
                        'db': 'wishlist',
                        'charset': 'utf8mb4',
                        'cursorclass': DictCursor}

    def create_table(self):
        with closing(pymysql.connect(**self.options)) as connection:
            with connection.cursor() as cursor:
                query = """
                CREATE TABLE IF NOT EXISTS
                wishlist (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                price FLOAT(2),
                url TEXT,
                comment TEXT
                )"""
                cursor.execute(query)
                connection.commit()

    def read_all(self) -> list:
        """Returns data as list of dicts {"id": int, "name": str, "price": float, "url": str, "comment": str}"""
        with closing(pymysql.connect(**self.options)) as connection:
            with connection.cursor() as cursor:
                query = """
                SELECT * from wishlist"""
                cursor.execute(query)
                data = []
                for row in cursor:
                    data.append(row)
        return data

    def read_row(self, row_id: int):
        """Returns row as dict {"id": int, "name": str, "price": float, "url": str, "comment": str}"""
        with closing(pymysql.connect(**self.options)) as connection:
            with connection.cursor() as cursor:
                query = f"""
                SELECT * from wishlist WHERE id = {row_id}"""
                cursor.execute(query)
        return cursor.fetchone()

    def add_row(self, name='', price=0, url='', comment='') -> int:
        """Returns id of inserted row"""
        with closing(pymysql.connect(**self.options)) as connection:
            with connection.cursor() as cursor:
                query = """
                INSERT INTO wishlist (name, price, url, comment) VALUES
                (%s, %s, %s, %s)"""
                values = (name, price, url, comment)
                cursor.execute(query, values)
                connection.commit()
                query = """SELECT LAST_INSERT_ID()"""
                cursor.execute(query)
                last_id = cursor.fetchone()['LAST_INSERT_ID()']
        return last_id

    def update_row(self, row_id, name=None, price=None, url=None, comment=None):
        with closing(pymysql.connect(**self.options)) as connection:
            with connection.cursor() as cursor:
                if name:
                    query = """
                    UPDATE wishlist SET name = %s WHERE id = %s
                            """
                    values = (name, row_id)
                    cursor.execute(query, values)
                if price:
                    query = """
                    UPDATE wishlist SET price = %s
                    WHERE id = %s
                            """
                    values = (price, row_id)
                    cursor.execute(query, values)
                if url:
                    query = """
                    UPDATE wishlist SET url = %s
                    WHERE id = %s
                            """
                    values = (url, row_id)
                    cursor.execute(query, values)
                if comment:
                    query = """
                    UPDATE wishlist SET comment = %s
                    WHERE id = %s
                            """
                    values = (comment, row_id)
                    cursor.execute(query, values)
                connection.commit()

    def delete_row(self, row_id: int):
        with closing(pymysql.connect(**self.options)) as connection:
            with connection.cursor() as cursor:
                query = f"""
                DELETE FROM wishlist  WHERE id = {row_id}
                        """
                cursor.execute(query)
                connection.commit()

    def drop_table(self):
        with closing(pymysql.connect(**self.options)) as connection:
            with connection.cursor() as cursor:
                query = f"""
                DROP TABLE IF EXISTS wishlist
                        """
                cursor.execute(query)
                connection.commit()


if __name__ == "__main__":
    db = Database()
    db.drop_table()
    db.create_table()
    db.add_row("HyperX Fury RGB [SHFR200/960G]", 5149, "https://www.dns-shop.ru/product/f9124fc4b98e3330/960-gb-ssd-nakopitel-hyperx-fury-rgb-shfr200960g/", "SSD 960 гб")
    db.add_row("Polaris PCM 1529E", 4990, "https://pokupki.market.yandex.ru/product/kofevarka-rozhkovaia-polaris-pcm-1529e-adore-crema-bezhevyi/100475689546?offerid=SlghgMxL31Kk3xh_EU6QVg&utm_source=market&utm_medium=cpc&utm_term=493303.000242.8881&utm_content=90589&clid=910&ymclid=16019801806443949868000004&from_beru=1", "Кофеварка рожковая")
    db.add_row("Clean Code: A Handbook of Agile Software Craftsmanship", 36.98, "https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882", " 1st Edition")
    db.add_row("ГРУША-XXXL", 1890, "https://vinni-puf.ru/grusha-xxxl-poliehster-zelenyj", "Зелёная, со скидкой.")
    db.add_row("SAWAJ 2", 27500, "https://palatka-online.ru/sawaj-2-palatka", "Прочная, лёгкая палатка на двоих")

