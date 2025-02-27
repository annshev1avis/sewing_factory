import os

import dotenv
import pymysql


dotenv.load_dotenv()


class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE")
        )

        self.cursor = self.conn.cursor()


    def get_materials(self):
        self.cursor.execute(
            'select distinct material_name'
            ' from write_off_with_material_data'
        )

        res = [x for (x,) in self.cursor.fetchall()]
        return res

    def get_reasons(self):
        self.cursor.execute(
            'select distinct reason'
            ' from write_off_with_material_data'
        )

        res = [x for (x,) in self.cursor.fetchall()]
        return res

    def get_write_offs(self, material=None, reason=None):
        query = """
            SELECT material_name, width, length,
            quantity, reason, timestamp, quantity * purchase_price
            FROM write_off_with_material_data
            WHERE can_be_used = false
        """
        params = []

        if material and material != 'Все':
            query += " AND material_name = %s"
            params.append(material)
        if reason and reason != 'Все':
            query += " AND reason = %s"
            params.append(reason)

        self.cursor.execute(query, params)
        result = self.cursor.fetchall()
        return result
