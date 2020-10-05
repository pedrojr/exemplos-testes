import psycopg2
import csv

def csv2pg():
    conn = None
    try:
		conn = psycopg2.connect(
		    host="localhost", database="test-csv", user="postgres", password="postgres")
		cursor = conn.cursor()

		cursor.execute("DROP TABLE IF EXISTS py_csv_pgsql;")
		cursor.execute("CREATE TABLE py_csv_pgsql (id int PRIMARY KEY, name text, num int);")
		conn.commit()

		with open('py_csv_pgsql.csv', 'r') as arquivo_csv:
		    leitor = csv.reader(arquivo_csv, delimiter=';')
		    for colunas in leitor:
		        cursor.execute("INSERT INTO py_csv_pgsql (id, name, num) VALUES (%s, %s, %s)",(colunas[0], colunas[1], colunas[2]))
		    conn.commit()

		cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    csv2pg()
