import sqlite3

DataBase = sqlite3.connect("D:\\MyWorks\\CasinoBot\\CasinoBaseData\\CasinoBD.db")
sqlite_create_table = """CREATE TABLE CasinoTable (
id INTEGER PRIMARY KEY,
balance MEDIUMINT UNSIGNED DEFAULT 0,
bet MEDIUMINT UNSIGNED DEFAULT 100,
qiwi_wallet TEXT,
btc_wallet TEXT,
ban BOOLEAN DEFAULT False);"""
cursor = DataBase.cursor()
cursor.execute(sqlite_create_table)
DataBase.commit()
cursor.close()
