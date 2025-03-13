running sql:
    docker-compose down
    docker-compose up -d        

view the sql:
    docker exec -it mysql-container mysql -u root -p
    Password:  my-secret-pw

running api:
    source venv/bin/activate
    python3 app.py

Test for sql:
    docker-compose down -v
    docker-compose up -d
    docker exec -it mysql-container mysql -u root -pmy-secret-pw my_database

Local:
    mysql -u root -pmy-secret-pw -h 127.0.0.1 -P 9090 my_database

For adding:
    curl -X GET http://127.0.0.1:5001/workout               
    [
        {
        "equipementused": "Dumbbells, Barbell",
        "id": 2,
        "musclegroup": "Legs",
        "videolink": "https://example.com/leg-workout-video",
        "workoutname": "Leg Day Routine"
        }
    ]

For deleting:
    curl -X DELETE http://localhost:5001/workout/Leg%20Day%20Routine

View all:
    curl -X GET http://127.0.0.1:5001/workout    