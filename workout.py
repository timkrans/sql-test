from flask import Flask, request, jsonify
from flask_cors import CORS 
import mysql.connector


# Initialize Flask app
app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:3000"])

# Connect to MySQL Database
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',        # MySQL host (use 'mysql-container' if Docker)
        port=9090,   
        user='root',             # MySQL username
        password='my-secret-pw', # MySQL root password
        database='my_database'   # The database you want to connect to
    )
    return connection

# Route to get all users
@app.route('/workout', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM workout;')
    workout = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(workout)

@app.route('/workout', methods=['POST'])
def create_user():
    new_workout = request.get_json()
    musclegroup = new_workout['musclegroup']
    videolink = new_workout['videolink']
    equipementused = new_workout['equipementused']
    workoutname = new_workout['workoutname']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO workout (musclegroup, videolink ,equipementused,  workoutname ) VALUES (%s, %s,%s,%s)', (musclegroup ,videolink,equipementused , workoutname))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/workout/<string:name>', methods=['DELETE'])
def delete_user(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM workout WHERE workoutname = %s', (name,))
    conn.commit()
    
    # Check if any row was deleted
    if cursor.rowcount == 0:
        return jsonify({"message": "User not found"}), 404
    
    cursor.close()
    conn.close()
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)