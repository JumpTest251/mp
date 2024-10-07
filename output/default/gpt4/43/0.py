from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('temperature_data.db')  # Replace with your database file
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    if not latitude or not longitude or not date:
        return jsonify({'error': 'Missing parameters'}), 400

    conn = get_db_connection()
    query = '''
        SELECT temperature 
        FROM temperature_records 
        WHERE latitude = ? AND longitude = ? AND date = ?
    '''
    cursor = conn.execute(query, (latitude, longitude, date))
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({'temperature': result['temperature']}), 200
    else:
        return jsonify({'error': 'No data found for the given parameters'}), 404

if __name__ == '__main__':
    app.run(debug=True)