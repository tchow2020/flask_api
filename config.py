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

self = banco.cursor()

# self.execute("create table usuario_empresa (id int (1) not null primary key auto_increment, usuario_id int (50), empresa_id int (50))")