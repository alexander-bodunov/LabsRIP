from django.db import models
import pymysql as MySQLdb1
import pymysql
from django.shortcuts import render


data={
    'books':[]
}

# Create your models here.
class Connection:
    def __init__(self, user, password, db, host='127.0.0.1'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self.charset="utf8"
        self._connection =None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):

        if not self._connection:
            self._connection = MySQLdb1.connect(
                user = self.user,
                host = self.host,
                passwd = self.password,
                db = self.db,
            )
        return self._connection
    def disconnect(self):
        if self._connection:
            self._connection.close()


class Book:
    def __init__(self,db_connection,id=1,name="a",author="a",description="a"):
        self.db_connection=db_connection#.connection()
        self.id=id
        self.name=name
        self.author=author
        self.description=description
        #self.c=self.db_connection.cursor(pymysql.cursors.DictCursor)
        #self.c = self.db_connection.cursor()

    def save(self):
        c = self.db_connection.cursor(pymysql.cursors.DictCursor)
        #c.execute("DELETE FROM Books WHERE id>0")
        c.execute("""INSERT INTO Books
               (id,name, author, description)
               VALUES
               (%s,%s, %s, %s)""",
               #(%s,%s, %s, %s)""",
               (self.id,self.name, self.author, self.description)
               )

        self.db_connection.commit()
        c.close()
    def _get_all(self):
        c = self.db_connection.cursor(pymysql.cursors.DictCursor)
        c.execute("SELECT * FROM Books")
        return c.fetchall()
    def _get_one(self,req_id):
        c = self.db_connection.cursor(pymysql.cursors.DictCursor)
        c.execute("SELECT * FROM Books WHERE id ="+str(req_id))
        return c.fetchall()
    def _clear_all(self,request):
        c = self.db_connection.cursor(pymysql.cursors.DictCursor)
        c.execute("DELETE FROM Books")
        #c.execute("UPDATE Books")
        c.execute("SELECT * FROM Books")
        self.db_connection.commit()

        check_all=c.fetchall()
        #check_all=c.self._get_all()
        data['books']=[]
        for check in check_all:
            data['books'].append(check)
        c.close()
        return render(request, 'books.html',data)


class Shop(models.Model):
    name=models.CharField(max_length=20)


'''
con = Connection("root","toshiba19","lab6")
db_connection=con.connect()
b=Book(db_connection,1,"Fan", "Asic Asimov", "simple")
b.save()
b=Book(db_connection,2,"Fan", "Asic Asimov", "simple")
b.save()
for i in b._get_all():
    print(i)

print('aaaa')

for i in b._get_one(2):
    print(i)

'''