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
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    name = new_user['name']
    email = new_user['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User created successfully"}), 201

# Route to update a user by id
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    updated_user = request.get_json()
    name = updated_user['name']
    email = updated_user['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (name, email, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User updated successfully"}), 200

# Route to delete a user by id
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
