import psycopg2
#Data
host = "localhost"
dbname = "Lista"
user = "postgres"
password = "manuele203"

#Conection
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

def create_object(nome,quantidade,preco):
    cursor.execute("insert into lista_objetos (nome,quantidade,preco) values (%s,%s,%s);", (nome,quantidade,preco))

create_object('mamao',1,2.90)

def update_object()

conn.commit()
cursor.close()
conn.close()