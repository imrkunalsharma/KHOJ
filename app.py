from flask import Flask, render_template, request, redirect
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    time = request.form['time']
    reason = request.form['reason']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO appointments (name, email, date, time, reason)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, email, date, time, reason))
    conn.commit()
    cursor.close()
    conn.close()
    
    return render_template('confirm.html', name=name, date=date, time=time)

@app.route('/admin')
def admin():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM appointments ORDER BY date, time")
    appointments = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('admin.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)
