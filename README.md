# GDSC-WEBDEV-TASK
This is the backend task for gdsc

Bonus task has been attempted and i have used a sqlite databse to store the names of the songs and artists

Added a delete method that deletes songs from the database

INSTALATION

    1.clone this git repo

    2.install packages by running pip install flask

    3.navigate to the project directory and running "flask run" in the terminal

    4.test this code using API platforms like POSTMAN and copying the localhost url that "flask run" gives you

API END POINTS

URL: /

Method: GET

Description: Displays a welcome message and directs users to the /music endpoint.

Music Endpoint

URL: /music

Methods: GET, POST, DELETE

GET Request

    Description: Retrieves all songs and artists from the database.

    Response: A JSON array of objects, each containing song and artist fields.

POST Request

    Description: Adds a new song and artist to the database.

    Data Fields:
        song: Name of the song
        artist: Name of the artist

DELETE Request

    Description: Deletes a song from the database and returns and error if song does not exist in database

    Data Fields:
        song: Name of song

Database

The application uses SQLite as its database, which is stored in a file named data.db. The music table should be set up with two columns: song (TEXT) and artist (TEXT).
There is aldredy dummy data in this table so you can start testing the api right away and you do not need to insert any data into the table
