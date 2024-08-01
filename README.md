# GDSC-WEBDEV-TASK
This is the backend task for gdsc

INSTALATION
1.clone this git repo
2.install packages by running pip install flask
3.run this command by navigate to the project directory and running "flask run" in the terminal
3.test this code using API platforms like POSTMAN and copying the localhost url that "flask  run" gives you

API END POINTS
URL: /
Method: GET
Description: Displays a welcome message and directs users to the /music endpoint.

Music Endpoint

URL: /music
Methods: GET, POST

GET Request

    Description: Retrieves all songs and artists from the database.

    Response: A JSON array of objects, each containing song and artist fields.

POST Request

    Description: Adds a new song and artist to the database.

    Data Fields:
        song: Name of the song
        artist: Name of the artist

Database

The application uses SQLite as its database, which is stored in a file named data.db. The music table should be set up with two columns: song (TEXT) and artist (TEXT).
