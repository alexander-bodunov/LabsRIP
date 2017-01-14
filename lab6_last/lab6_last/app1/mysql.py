__author__ = 'Work'
import pymysql

db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="toshiba19",
    db="lab6",
    charset="utf8"
)

cursor = db.cursor(pymysql.cursors.DictCursor)

cursor.execute("DELETE FROM Books WHERE id>0")

cursor.execute("""INSERT INTO Books
               (id,name, author, description)
               VALUES
               (%s,%s, %s, %s),
               (%s,%s, %s, %s)""",
               (1,"Война и Мир", "Лев Толстой", "Классика",
                2,"Буря мечей", "Джордж Мартин", "Топ")
               )

db.commit()

cursor.execute("SELECT * FROM Books")

books = cursor.fetchall()

for book in books:
    print("{}: {} {} {}".format(book['id'],book['name'],book['author'],book['description']))

#for b in books:
 #   for a in b:
 #       print(a),

#cursor.execute("DELETE FROM Books WHERE id>5")
db.commit()

cursor.close()
db.close()
