from flask import Flask,request,jsonify
import sqlite3

app=Flask(__name__)
@app.route("/")
def index():
    return jsonify("Congrats on getting my code to run. the api endpoint is set to /music so switch to that url and check out my GET, POST and DELETE ENDPOINTS")

@app.route("/music",methods=["GET","POST","DELETE"])
def music():
    con = sqlite3.connect("data.db")

    
    if request.method=="GET":
        cur = con.cursor()
        #selects the entire table from the db
        temp=cur.execute("SELECT * from music")
        data=temp.fetchall()
        
        #initializing the dict to have a key:value pair in json
        music_dict={}
        #initialising list so that we can jsonify all the songs and return that json
        music_list=[]

        #traversing through all the data and making proper key value pairs
        #from them and adding them to the final data list to be jsonified
        for row in data:
            music_dict["song"]=row[0]
            music_dict["artist"]=row[1]
            music_list.append(music_dict)
            music_dict={}
        cur.close()
        return jsonify(music_list)
    


    elif request.method=="POST":
        new_song=request.form.get("song")
        new_artist=request.form.get("artist")
        cur = con.cursor()
        #error handling
        if not new_song or not new_artist:
                return jsonify({"error": "Missing 'song' or 'artist'"}), 400
        #adding the new song values into the table and commiting them so that he gets saved in the table
        try:
                cur.execute("INSERT INTO music (song, artist) VALUES (?, ?)", (new_song, new_artist))
                con.commit()
                return "Artist and song added successfully to the database", 200
        except sqlite3.Error as e:
                return jsonify({"error": str(e)}), 500
        finally:
                cur.close()
    
    
    #deleting song from database
    elif request.method=="DELETE":
        song=request.form.get("song")
        if song:
            cur=con.cursor()
            #checks if song exists in database or not
            cur.execute("SELECT 1 from music where song=?",(song,))
            result=cur.fetchone()
            if result:
                cur.execute("DELETE FROM music where song=?",(song,))
                con.commit()
                return jsonify("Song deleted successfully")
            else:
                return jsonify("song did not exist in table")
        else:
            return jsonify({"error": "Missing 'song'"}), 400
            





if __name__=="__main__":
    app.run()











