import sqlite3
import alpaca_trade_api as tradeapi

connection = sqlite3.connect('app.db')
connection.row_factory = sqlite3.Row
# connects alpaca api to retrive data

cursor = connection.cursor()


cursor.execute("""
    SELECT symbol, company FROM stock
""")



rows = cursor.fetchall()
symbols = [row['symbol'] for row in rows]

api = tradeapi.REST('PKJMX8YJFVQR8ZB2KNRV', 'mYfZfbjjFiYt6pE2hityq8fU5EhdH0LWsGuYd8g1', api_version='v2', base_url='https://paper-api.alpaca.markets')
assets = api.list_assets()



for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
            print(f"added a new stokc {asset.symbol} {asset.name}")
            # cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)






connection.commit()
