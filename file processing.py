#ive done like 0 of this dont judge
import musicbrainzngs
import re
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
  database="mydatabase"
)

#insert user input into UploadLog table

#website identifier for queries
musicbrainzngs.set_useragent(
    "SpekCheck",
    "Alpha 1.0",
    "EMAIL",
)

#fetch metadata from MusicBrainz
release_id = WEBFORM INPUT
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
