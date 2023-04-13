import sqlite3

conn = sqlite3.connect('stats.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE stats(
           id INTEGER PRIMARY KEY ASC, 
           max_buy_price FLOAT NOT NULL,
           num_buys INTEGER NOT NULL,
           max_sell_price FLOAT NOT NULL,
           num_sells INTEGER NOT NULL,
           last_updated VARCHAR(250) NOT NULL)
          ''')

c.execute('''
          INSERT INTO stats values(
            1,
            0.00,
            0,
            0.00,
            0,
            "1970-01-01T00:00:00Z")
          ''')

conn.commit()
conn.close()