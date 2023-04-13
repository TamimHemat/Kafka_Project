import mysql.connector

db_conn = mysql.connector.connect(host="localhost", user="root", password="tamimmysql", database="events")
db_cursor = db_conn.cursor()

db_cursor.execute('''
    CREATE TABLE buy
    (id INT NOT NULL AUTO_INCREMENT,
    buy_id VARCHAR(250) NOT NULL,
    item_name VARCHAR(250) NOT NULL,
    item_price FLOAT NOT NULL,
    buy_qty INTEGER NOT NULL,
    trace_id VARCHAR(100) NOT NULL,
    date_created VARCHAR(100) NOT NULL,
    CONSTRAINT buy_pk PRIMARY KEY (id))
''')

db_cursor.execute('''
    CREATE TABLE sell
    (id INT NOT NULL AUTO_INCREMENT,
    sell_id VARCHAR(250) NOT NULL,
    item_name VARCHAR(250) NOT NULL,
    item_price FLOAT NOT NULL,
    sell_qty INTEGER NOT NULL,
    trace_id VARCHAR(100) NOT NULL,
    date_created VARCHAR(100) NOT NULL,
    CONSTRAINT sell_pk PRIMARY KEY (id))
''')

db_conn.commit()
db_conn.close()