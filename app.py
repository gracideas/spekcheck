#!C:\Python27\python.exe -u

import MySQLdb as mysql

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def spekcheck():
    return 'here goes the home page'

@app.route('/form', methods=['POST', 'GET'])
def form():
    message = ''
    if request.method == 'POST':
        musicbrainz_id = request.form.get('musicbrainz_id', 0)
        source = request.form.get('source', 0)
        fileitem = request.form.get('filename', 0)

        #form validation
        mbidCheck = len('musicbrainz_id')
        sourceCheck = source.isupper() or source.islower()

        #run duplicate check
        mydb = mysql.connect(
          host="localhost",
          user="yourusername",
          passwd="yourpassword",
          database="mydatabase"
        )

        mycursor = mydb.cursor()

        sql = "SELECT * FROM SpecMetadata WHERE MusicBrainzID = %s" #prevent sql injection

        mycursor.execute(sql, musicbrainz_id)

        existingEntry = mycursor.rowcount(mycursor.fetchall())

        if existingEntry != 0: #entry already exists
            message = "entry already exists"

        if mbidCheck < 36:
            message = musicbrainz_id + ' is not a valid MusicBrainz ID'
        if sourceCheck == False:
            message = 'You must include a source'
        if fileitem.filename:
            # strip leading path from file name to avoid
            # directory traversal attacks
            fn = os.path.basename(fileitem.filename)
            open('/tmp/' + fn, 'wb').write(fileitem.file.read())

        #check MBID against existing entries in database

        else:
            message = 'Entry submitted'



        #
        import musicbrainzngs
        import re

        #perform duplicate entry checks WIP

        #insert user input into UploadLog table

        #website identifier for queries
        musicbrainzngs.set_useragent(
            "SpekCheck",
            "Alpha 1.0",
            "EMAIL",
        )

        #fetch metadata from MusicBrainz
        release_id = musicbrainz_id
        try:
            result = musicbrainzngs.get_release_by_id(release_id, includes=["artist", "label", "discid"], )
        except WebServiceError as exc:
            print("Something went wrong with the request: %s" % exc)
        else:
            release = ["release"]
            artist = ["artist"]
            label = ["label"]
            catalogNo = ["discid"]

        #insert user input into UploadLog table WIP
        mycursor = mydb.cursor()

        sql = "INSERT INTO UploadLog (Uploader,MusicBrainzID,Source) VALUES (%s, %s)"
        val = ("WEBFORM INPUT", "WEBFORM INPUT", "WEBFORM INPUT")
        mycursor.executemany(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        #insert fetched data into Metadata table WIP
        mycursor = mydb.cursor()

        sql = "INSERT INTO Metadata (COLUMN NAME, COLUMN NAME) VALUES (%s, %s)"
        val = ("WEBFORM INPUT")
        mycursor.executemany(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        #call ffmpeg to produce the spectogram of audio files
        import os

        import subprocess
        os.chdir('DIRECTORY')
        subprocess.run(['for %%a in *.flac *.alac *.wav *.aac *.wma *.opus *.m4a *.ape do ffmpeg -i "%%a" -lavfi showspectrumpic=s=1920x1080 "%%~na.png" -n'])

        #insert spectogram into respective table

    # serve static page
    return render_template('submit.html', message=message)

@app.route('/guidelines')
def guidelines():
    return render_template('guidelines.html')

@app.route('/display')
def display():
    return render_template('display.html')
