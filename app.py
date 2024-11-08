from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='password',
        database='testdb'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT "Hello, World!"')
    result = cursor.fetchone()
    conn.close()
    return result[0]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
