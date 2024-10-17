from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    conn = get_db_connection()
    cur = conn.cursor()
    
    query = '''SELECT temperature FROM temperatures 
               WHERE latitude = ? AND longitude = ? AND date = ?'''
    cur.execute(query, (latitude, longitude, date))
    
    result = cur.fetchone()
    conn.close()

    if result is not None:
        temperature = result['temperature']
        return jsonify({'temperature': temperature}), 200
    else:
        return jsonify({'error': 'Temperature not found for the specified location and date.'}), 404

if __name__ == '__main__':
    app.run(debug=True)