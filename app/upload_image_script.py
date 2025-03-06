import pymysql

def upload_image_to_db(image_path, db_config):
    try:
        # Подключение к базе данных
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            charset='utf8mb4'
        )
        cursor = connection.cursor()

        # Чтение изображения в бинарном режиме
        with open(image_path, 'rb') as file:
            binary_data = file.read()

        # SQL-запрос на вставку изображения
        query = """
        INSERT INTO product_type (photo) VALUES (%s)
        """
        cursor.execute(query, (binary_data,))
        connection.commit()
        print("Изображение успешно загружено в базу данных.")

    except pymysql.MySQLError as e:
        print("Ошибка работы с MySQL:", e)
    finally:
        cursor.close()
        connection.close()

# Конфигурация базы данных
DB_CONFIG = {
    'host':"fatima6p.beget.tech",
    'user':"fatima6p_orange",
    'password':"m%Y2a3fkH1xE",
    'database':"fatima6p_orange"
}

# Путь к изображению
IMAGE_PATH = 'C:/Users/Anna/Pictures/пингвины.jpg'

# Вызов функции загрузки
upload_image_to_db(IMAGE_PATH, DB_CONFIG)