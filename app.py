from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gaur2005",
    database="library_management_system"
)
mycursor = mydb.cursor(dictionary=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books')
def books():
    mycursor.execute("SELECT * FROM books")
    books = mycursor.fetchall()
    return render_template('books.html', books=books)

@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        data = request.form
        mycursor.execute("INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s)",
                         (data['book_id'], data['book_name'], data['genre'], data['authors_name'], data['language'], data['quantity']))
        mydb.commit()
        return redirect(url_for('books'))
    return render_template('add_book.html')

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    mycursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
    mydb.commit()
    return redirect(url_for('books'))

@app.route('/cardholders')
def cardholders():
    mycursor.execute("SELECT * FROM card_holders")
    cards = mycursor.fetchall()
    return render_template('cardholders.html', cards=cards)

@app.route('/add_cardholder', methods=['GET', 'POST'])
def add_cardholder():
    if request.method == 'POST':
        data = request.form
        mycursor.execute("INSERT INTO card_holders VALUES (%s, %s, %s, %s, %s)",
                         (data['card_no'], data['name'], data['phone_no'], data['address'], data['dob']))
        mydb.commit()
        return redirect(url_for('cardholders'))
    return render_template('add_cardholder.html')

@app.route('/lend_book', methods=['GET', 'POST'])
def lend_book():
    if request.method == 'POST':
        data = request.form
        mycursor.execute("""
            INSERT INTO library_transactions (card_no, book_id, book_name, issue_date, return_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['card_no'], data['book_id'], data['book_name'], data['issue_date'], data['return_date']))
        mydb.commit()
        return redirect(url_for('home'))
    return render_template('lend_book.html')

@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        card_no = request.form['card_no']
        return_date = request.form['return_date']
        mycursor.execute("""
            UPDATE library_transactions
            SET return_date = %s
            WHERE card_no = %s AND return_date = '0000-00-00'
        """, (return_date, card_no))
        mydb.commit()
        return redirect(url_for('home'))
    return render_template('return_book.html')

@app.route('/lending_history', methods=['GET', 'POST'])
def lending_history():
    records = []
    if request.method == 'POST':
        card_no = request.form['card_no']
        mycursor.execute("""
            SELECT book_name, issue_date, return_date
            FROM library_transactions
            WHERE card_no = %s
        """, (card_no,))
        records = mycursor.fetchall()
    return render_template('lending_history.html', records=records)

@app.route('/order_book', methods=['GET', 'POST'])
def order_book():
    if request.method == 'POST':
        data = request.form
        mycursor.execute("""
            INSERT INTO ordered_books (order_id, book_name, delivery_date, price, quantity)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['order_id'], data['book_name'], data['delivery_date'], data['price'], data['quantity']))
        mydb.commit()
        return redirect(url_for('home'))
    return render_template('order_book.html')

if __name__ == '__main__':
    app.run(debug=True)