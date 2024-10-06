from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root_123',
        database='swell_wave'
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data') # Make this location 1
def data():

    # Specify location
    location1Query = "SELECT * FROM swelldata WHERE latitude BETWEEN 7.10321 AND 7.10341 AND longitude BETWEEN 125.7189 AND 125.7191"
    location2Query = "SELECT * FROM SwellData WHERE latitude BETWEEN 54.544487 AND 54.544687 AND longitude BETWEEN 10.227387 AND 10.227587"

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # cursor.execute("SELECT * FROM swelldata WHERE latitude=7.10331 and longitude=125.719")
    cursor.execute(location2Query)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
