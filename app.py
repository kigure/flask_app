from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import db

database = 'database.db'
db.create_book_table()

app = Flask(__name__)


@app.route('/')
def index():
    con = sqlite3.connect(database)
    db_book = con.execute('SELECT * FROM book').fetchall()
    con.close()

    book = []
    for row in db_book:
        book.append({'title': row[0], 'price': row[1], 'arrival_day': row[2]})

    return render_template('index.html', book=book)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(database)
    con.execute('INSERT INTO book VALUES(?, ?, ?)',
                [title, price, arrival_day])
    con.commit()
    con.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
