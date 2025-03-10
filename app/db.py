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
            database=os.getenv("DATABASE"),
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

    def get_unusable_write_offs(self, material=None, reason=None):
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

    def get_usable_write_offs(self, material, sort_order):
        if material == "Все":
            query = f"""
                select material_name, quantity, width, length, width * length, 
                timestamp, purchase_price * quantity
                from write_off_with_material_data
                where can_be_used = True
                order by width * length {sort_order}
            """
            self.cursor.execute(query)
        else:
            query = f"""
                select material_name, quantity, width, length, width * length, 
                timestamp, purchase_price * quantity
                from write_off_with_material_data
                where can_be_used = True and material_name = "{material}"
                order by width * length {sort_order}
            """
            self.cursor.execute(query)

        return self.cursor.fetchall()

    def add_role(self, role_name):
        query = "INSERT INTO role (role_name) VALUES (%s)"
        self.cursor.execute(query, (role_name,))
        self.conn.commit()

    def get_roles(self):
        query = "SELECT id, role_name FROM role"
        self.cursor.execute(query)
        roles = self.cursor.fetchall()

        return roles

    def add_worker(self, sur, name, patr, log, pas, role_id):
        query = """
            INSERT INTO worker (surname, name, patronymic, login, password, id_role)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (sur, name, patr, log, pas, role_id))
        self.conn.commit()

    def get_textile_materials(self):
        query = """
                    select distinct m.name 
                    from material m inner join material_category cat on m.id_category = cat.id
                    where cat.name = "Ткань" 
                """
        self.cursor.execute(query)
        return  [material[0] for material in self.cursor.fetchall()]

    def close(self):
        self.cursor.close()
        self.conn.close()
