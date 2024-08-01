from flask import Flask,request,jsonify
import sqlite3

app=Flask(__name__)
@app.route("/")
def index():
    return("hello world hi lol")

@app.route("/test",methods=["GET","POST"])
def music():
    con = sqlite3.connect("data.db")
    if request.method=="GET":
        cur = con.cursor()
        temp=cur.execute("SELECT * from music")
        data=temp.fetchall()
        print(data)
        music_dict={}
        music_list=[]
        for row in data:
            music_dict["song"]=row[0]
            music_dict["artist"]=row[1]
            music_list.append(music_dict)
            music_dict={}
        return jsonify(music_list)
    

    if request.method=="POST":
        new_song=request.form["song"]
        new_artist=request.form["artist"]
        cur = con.cursor()
        temp=cur.execute("INSERT INTO music(song,artist)VALUES(?,?)",(new_song,new_artist))
        con.commit()
        return "artist added successfully to database",200

if __name__=="__main__":
    app.run()











