import os

import dotenv
import pymysql


dotenv.load_dotenv()


class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            # host=os.getenv("HOST"),
            # user=os.getenv("USER"),
            # password=os.getenv("PASSWORD"),
            # database=os.getenv("DATABASE")
            host='localhost',
            user='root',
            password='',
            database='sewing_factory'
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

    def get_personal_data(self, username, password):
        query = "SELECT * FROM worker WHERE login = %s AND password = %s"
        self.cursor.execute(query, (username, password))
        res = self.cursor.fetchone()

        if res:
            query = "SELECT id_role FROM worker WHERE login = %s AND password = %s"
            self.cursor.execute(query, (username, password))
            role = self.cursor.fetchone()[0]
            return res, role

        return res

    def add_pos(self, pos_name):
        query = "INSERT INTO role (role_name) VALUES (%s)"
        self.cursor.execute(query, (pos_name,))
        self.conn.commit()

    def get_positions(self):

        query = "SELECT id, role_name FROM role"
        self.cursor.execute(query)
        positions = self.cursor.fetchall()

        return positions

    def add_worker(self, sur,name, patr, log, pas, role_id):
        query = """
            INSERT INTO worker (surname, name, patronymic, login, password, id_role)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (sur, name, patr, log, pas, role_id))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
