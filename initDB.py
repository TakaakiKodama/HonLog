# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String
import datetime
from app import BookInfo
from app import db
import random, string

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)
# print(randomname(10))

db.drop_all()
db.create_all()

for i in range(100):
    bookId=BookInfo()
    bookId.ID=randomname(10)
    bookId.date=datetime.date.today()
    bookId.datetime=datetime.datetime.now()
    bookId.title=randomname(15)
    bookId.auth=randomname(8)
    bookId.review=randomname(100)
    db.session.add(bookId)
    db.session.commit()
