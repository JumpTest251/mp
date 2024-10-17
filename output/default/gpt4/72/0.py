from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_max_temperature(latitude, longitude, year, month, day, grib_file):
    conn = mysql.connector.connect(
        host='your_db_host',
        user='your_db_user',
        password='your_db_password',
        database='your_db_name'
    )
    cursor = conn.cursor(dictionary=True)
    
    query = """
    SELECT MAX(temperature) AS max_temperature
    FROM temperature_data
    WHERE latitude = %s AND longitude = %s AND year = %s AND month = %s AND day = %s AND grib_file = %s
    """
    cursor.execute(query, (latitude, longitude, year, month, day, grib_file))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return result['max_temperature'] if result else None

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    grib_file = request.args.get('grib_file')
    
    if not all([latitude, longitude, year, month, day, grib_file]):
        return jsonify({"error": "Missing parameters"}), 400

    max_temperature = get_max_temperature(latitude, longitude, year, month, day, grib_file)
    
    if max_temperature is not None:
        return jsonify({"max_temperature": max_temperature}), 200
    else:
        return jsonify({"error": "No data found"}), 404

if __name__ == '__main__':
    app.run(debug=True)