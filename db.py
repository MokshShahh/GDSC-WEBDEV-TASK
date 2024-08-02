#used these commands to make and fill my db with dummy content so that get requests has something to show

import sqlite3
con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("delete from music")
cur.execute("CREATE TABLE IF NOT EXISTS music(song, artist)")
cur.execute("""INSERT INTO music(song,artist) 
            VALUES
            ('In my room','Frank Ocean'),
            ('The less i know the better','Tame Impala'),
            ('Chamber of reflection','Mac Demarco')""")
song="In my room"

cur.execute("SELECT 1 from music where song=?",(song,))
result=cur.fetchone()
if result:
    cur.execute("DELETE FROM music where song=?",(song,))
else:
    print("song did not exist in table")

cur.execute("commit")



print(cur.execute("select * from music").fetchall())