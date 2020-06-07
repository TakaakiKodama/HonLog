from flask import Flask, render_template, request,  redirect, url_for # 必要なライブラリのインポート
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import random, string
import datetime
import os
app = Flask(__name__)  # アプリの設定

app.config['SECRET_KEY'] = 'secret key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.sqlite' # DBへのパス
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

#SQLAlchemyでデータベース定義

db = SQLAlchemy(app)

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

class BookInfo(db.Model):
    __tablename__ = 'bookInfo'

    ID = db.Column(String(32), primary_key=True)
    date = db.Column(db.DateTime,nullable=False)
    datetime = db.Column(db.DateTime,nullable=False)
    title =db.Column(String(),nullable=False)
    auth =db.Column(String(),nullable=False)
    review =db.Column(String(),nullable=False)


@app.route("/")
def main():
    name = "Hoge"
    databaseList=BookInfo.query.all()
    # print(databaseList)
    return render_template("top.html", title='本ログTOP', name=name, database=databaseList)

@app.route("/bookreviwe/<bookid>")
def bookreviwe(bookid):
    bookdata=BookInfo.query.filter_by(ID=bookid).all()[0]
    # booktalk=bookthred[bookid]
    # return render_template("bookreview.html", title='レビュー', bookdata=bookdata,booktalk=booktalk)
    return render_template("bookreview.html", title='レビュー', bookdata=bookdata)

@app.route("/newreview", methods=["GET", "POST"])
def newreview():
    return render_template("newreview.html", title='新しいレビュー')

@app.route("/registnewreview", methods=["GET", "POST"])
def registnewreview():
    print(request.form["booktitle"],request.form["bookauth"],request.form["review"])
    bookId=BookInfo()
    bookId.ID=randomname(10)
    bookId.date=datetime.date.today()
    bookId.datetime=datetime.datetime.now()
    bookId.title=request.form["booktitle"]
    bookId.auth=request.form["bookauth"]
    bookId.review=request.form["review"]
    db.session.add(bookId)
    db.session.commit()

    return redirect(url_for('main'))

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='localhost', port=5000, threaded=True)  # デバッグモード、localhost:8888 で スレッドオンで実行
