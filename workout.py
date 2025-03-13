from flask import Flask, request, jsonify
import mysql.connector

# Initialize Flask app
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=5001)