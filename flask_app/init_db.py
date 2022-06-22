import os 
import psycopg2

conn = psycopg2.connect (
    host="localhost",
    dbname="Lista",
    user="postgres",
    password="manuele203")

#Perfom database 

cursor = conn.cursor()

#Insert into database

def create_object(nome,quantidade,preco):
    cursor.execute("insert into lista_objetos (nome,quantidade,preco) values (%s,%s,%s);", (nome,quantidade,preco))

create_object('mamao',1,2.90)


conn.commit()
cursor.close()
conn.close()