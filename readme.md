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
