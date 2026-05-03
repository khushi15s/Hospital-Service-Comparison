from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    city = request.form['city']
    service = request.form['service']

    conn = get_db_connection()

    hospitals = conn.execute(
        """
        SELECT * FROM hospital
        WHERE LOWER(city) LIKE LOWER(?)
        AND LOWER(service) LIKE LOWER(?)
        ORDER BY rating DESC
        """,
        ('%' + city + '%', '%' + service + '%')
    ).fetchall()

    conn.close()

    return render_template('results.html', hospitals=hospitals)

if __name__ == '__main__':
    app.run(debug=True)