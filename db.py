import pymysql


class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="sewing_factory"
        )
        self.cursor = self.conn.cursor()

    def get_materials(self):
        self.cursor.execute('select DISTINCT(name) from material '
                            'inner join write_off on write_off.material_id = material.id')

        res = [x for (x,) in self.cursor.fetchall()]
        return res

    def get_reasons(self):
        self.cursor.execute('select DISTINCT(reason) from write_off')

        res = [x for (x,) in self.cursor.fetchall()]
        return res

    def get_write_offs(self, material=None, reason=None):
        query = """
            SELECT material.name, write_off.width, write_off.length,
            write_off.quantity, write_off.reason, write_off.timestamp
            FROM write_off
            INNER JOIN material ON write_off.material_id = material.id
            WHERE write_off.can_be_used = false
        """
        params = []

        if material and material != 'Все':
            query += " AND material.name = %s"
            params.append(material)
        if reason and reason != 'Все':
            query += " AND write_off.reason = %s"
            params.append(reason)

        self.cursor.execute(query, params)
        result = self.cursor.fetchall()
        return result
