import psycopg2

class User:
    def money(id):
        conn = psycopg2.connect("dbname=ge_sales_dev user=postgres password=chyld host=127.0.0.1")
        cur = conn.cursor()
        cur.execute('SELECT * FROM "Sales" where user_id = ' + id + ';')
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
