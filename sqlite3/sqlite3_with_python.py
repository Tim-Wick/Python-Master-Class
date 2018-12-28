import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 123456789, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 456789123, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()
db.close()


import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "anotherotherupdate@update.com"
phone = input("Please enter the phone number ")
# SQL injection opportunity whe using update_cursor.executescript instead of just .execute by appending semi colon with
# command after input. "123456789;drop table contacts"

# update_sql = "UPDATE contacts SET email = '{}' WHERE phone={}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone=?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()

import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Please enter your name: ")

for row in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
    print(row)

# get_name = ("SELECT * FROM contacts WHERE name=?")
#
# name_cursor = db.cursor()
# name_cursor.execute(get_name, name)



db.close()
