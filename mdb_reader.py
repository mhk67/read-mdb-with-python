import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=./dbs/db_name.mdb;')
cursor = conn.cursor()

cursor.execute('SELECT * FROM table_name')
# cursor.execute('SELECT TOP 100 * FROM table_name')
# columns = [column[0] for column in cursor.description]
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()


