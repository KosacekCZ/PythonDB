import os
import db


connection = db.connect_db("/home/pesekmik/Downloads/db_priklady_skoleni/db_priklady_skoleni/SQLite/databaze_pro_web.db")
if connection is not None:
    cursor = connection.cursor()

    #db.add_user(cursor, "Mik", "mikolas.pesek@fel.cvut.cz", "Heslo123")
    db.get_users(cursor)
else:
    print("Neny databasa")


