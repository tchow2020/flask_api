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

# self.execute("create table empresas (id int (50) not null primary key auto_increment, nome varchar (100), status varchar (1))")