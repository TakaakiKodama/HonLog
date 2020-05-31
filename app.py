from flask import Flask, render_template # 必要なライブラリのインポート

app = Flask(__name__)  # アプリの設定

databaseList=[
    {"title":"七つの習慣","bookid":"sevenId"},
    {"title":"メモの魔力","bookid":"memo"},
    {"title":"イシューから始めよ","bookid":"issue"},
    {"title":"君の膵臓を食べたい","bookid":"kimisui"},
    {"title":"今更翼と言われても","bookid":"tsubasa"},
]
databaseDict={
    "sevenId":{"date":"2020-05-31","title":"七つの習慣","auth":"stevenRcoby","review":"すごい"},
    "memo":{"date":"2020-05-31","title":"メモの魔力","auth":"雄二","review":"よい"},
    "issue":{"date":"2020-05-31","title":"イシューから始めよ","auth":"すごい人","review":"大事"},
    "kimisui":{"date":"2020-05-31","title":"君の膵臓を食べたい","auth":"エモい人","review":"なける"},
    "tsubasa":{"date":"2020-05-31","title":"今更翼と言われても","auth":"よねざわほのぶ","review":"苦い"},
}
bookthred={
    "sevenId":["わかる","いいよね"],
    "memo":["わかる","いいよね"],
    "issue":["わかる","いいよね"],
    "kimisui":["わかる","いいよね"],
    "tsubasa":["わかる","いいよね"],
}

@app.route("/")
def main():
    name = "Hoge"
    return render_template("top.html", title='本ログTOP', name=name, database=databaseList)

@app.route("/bookreviwe/<bookid>")
def bookreviwe(bookid):
    bookdata=databaseDict[bookid]
    booktalk=bookthred[bookid]
    return render_template("bookreview.html", title='レビュー', bookdata=bookdata,booktalk=booktalk)


if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='localhost', port=5000, threaded=True)  # デバッグモード、localhost:8888 で スレッドオンで実行
