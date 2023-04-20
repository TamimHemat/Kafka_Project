import sqlite3

conn = sqlite3.connect('stats.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS stats(
           id INTEGER PRIMARY KEY ASC, 
           max_buy_price FLOAT NOT NULL,
           num_buys INTEGER NOT NULL,
           max_sell_price FLOAT NOT NULL,
           num_sells INTEGER NOT NULL,
           last_updated VARCHAR(250) NOT NULL)
          ''')

conn.commit()
conn.close()