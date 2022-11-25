import mariadb
import sys

try:
    banco = mariadb.connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='teste'
    )
    
except mariadb.Error as e:
    print(f"erro ao conectar no banco {e}")
    sys.exit(1)

# self = banco.cursor()

# self.execute("CREATE TABLE user (nome VARCHAR(50), email VARCHAR(50), id int NOT NULL PRIMARY KEY AUTO_INCREMENT)")