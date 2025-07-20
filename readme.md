# Workout Tracker API

A Flask-based REST API for managing workout routines with MySQL database backend. This application allows you to create, read, and delete workout entries with details like muscle groups, video links, and equipment used.

## 🚀 Features

- **RESTful API**: Full CRUD operations for workout management
- **MySQL Database**: Persistent data storage with Docker containerization
- **CORS Support**: Cross-origin resource sharing enabled for frontend integration
- **Docker Integration**: Easy setup and deployment with Docker Compose

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.7+
- MySQL client (optional, for direct database access)

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/timkrans/sql-test
cd sql-backend
```

### 2. Start the Database
```bash
# Start MySQL container
docker-compose up -d

# Verify the container is running
docker ps
```

### 3. Set Up Python Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install flask flask-cors mysql-connector-python
```

## 🏃‍♂️ Running the Application

### Start the API Server
```bash
# Make sure your virtual environment is activated
source venv/bin/activate

# Run the workout API (port 5001)
python workout.py

# Or run the user API (port 5000)
python app.py
```

The API will be available at:
- Workout API: http://127.0.0.1:5001
- User API: http://127.0.0.1:5000

## 🗄️ Database Management

### Access MySQL Database
```bash
# Connect to MySQL container
docker exec -it mysql-container mysql -u root -p
# Password: my-secret-pw

# Or connect directly to the database
docker exec -it mysql-container mysql -u root -pmy-secret-pw my_database
```

### Local Database Access
```bash
# Connect from host machine
mysql -u root -pmy-secret-pw -h 127.0.0.1 -P 9090 my_database
```

### Reset Database
```bash
# Stop and remove containers with volumes
docker-compose down -v

# Start fresh
docker-compose up -d
```

## 📚 API Endpoints

### Workout Management (`workout.py`)

#### Get All Workouts
```bash
curl -X GET http://127.0.0.1:5001/workout
```

**Response:**
```json
[
  {
    "id": 2,
    "workoutname": "Leg Day Routine",
    "musclegroup": "Legs",
    "videolink": "https://example.com/leg-workout-video",
    "equipementused": "Dumbbells, Barbell"
  }
]
```

#### Create New Workout
```bash
curl -X POST http://127.0.0.1:5001/workout \
  -H "Content-Type: application/json" \
  -d '{
    "workoutname": "Push Day",
    "musclegroup": "Chest, Triceps",
    "videolink": "https://example.com/push-workout",
    "equipementused": "Barbell, Bench"
  }'
```

#### Delete Workout by Name
```bash
curl -X DELETE http://127.0.0.1:5001/workout/Leg%20Day%20Routine
```

### User Management (`app.py`)

#### Get All Users
```bash
curl -X GET http://127.0.0.1:5000/users
```

#### Create New User
```bash
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com"
  }'
```

#### Update User
```bash
curl -X PUT http://127.0.0.1:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith",
    "email": "johnsmith@example.com"
  }'
```

#### Delete User
```bash
curl -X DELETE http://127.0.0.1:5000/users/1
```

## 🗂️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```

### Workout Table
```sql
CREATE TABLE workout (
    id INT AUTO_INCREMENT PRIMARY KEY,
    workoutname VARCHAR(100) NOT NULL,
    musclegroup VARCHAR(100) NOT NULL,
    videolink VARCHAR(100) NOT NULL,
    equipementused VARCHAR(100) NOT NULL
);
```

## 🔧 Configuration

### Environment Variables
- **MySQL Host**: `localhost` (or `mysql-container` for Docker)
- **MySQL Port**: `9090`
- **MySQL User**: `root`
- **MySQL Password**: `my-secret-pw`
- **Database Name**: `my_database`

### Docker Configuration
- **MySQL Container**: `mysql-container`
- **Host Port Mapping**: `9090:3306`
- **Data Persistence**: `mysql-data` volume

## 🧪 Testing

### Test Database Connection
```bash
# Start fresh database
docker-compose down -v
docker-compose up -d

# Test connection
docker exec -it mysql-container mysql -u root -pmy-secret-pw my_database
```

### Test API Endpoints
```bash
# Test workout API
curl -X GET http://127.0.0.1:5001/workout

# Test user API
curl -X GET http://127.0.0.1:5000/users
```

## 🚨 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Check what's using the port
   lsof -i :5001
   # Kill the process
   kill -9 <PID>
   ```

2. **Database Connection Failed**
   ```bash
   # Restart MySQL container
   docker-compose restart mysql
   ```

3. **Virtual Environment Issues**
   ```bash
   # Recreate virtual environment
   rm -rf venv
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## 📝 Development

### Project Structure
```
sql-backend/
├── app.py              # User management API
├── workout.py          # Workout management API
├── db/
│   └── schema.sql      # Database schema
├── docker-compose.yml  # Docker configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```
