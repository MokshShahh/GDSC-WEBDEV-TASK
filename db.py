# import sqlite3
# con = sqlite3.connect("data.db")
# cur = con.cursor()
# cur.execute("delete from music")
# cur.execute("CREATE TABLE IF NOT EXISTS music(song, artist)")
# # cur.execute("""INSERT INTO music(song,artist) 
# #             VALUES
# #             ('In my room','Frank Ocean'),
# #             ('The less i know the better','Tame Impala'),
# #             ('Chamber of reflection','Mac Demarco')""")
# # cur.execute("commit")

# print(cur.execute("select * from music").fetchall())