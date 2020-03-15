#connect to database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
  database="mydatabase"
)

#check MBID against existing entries

#perform duplicate entry checks

#fetch metadata from MusicBrainz

#insert fetched metadata into respective table

#insert user input into upload log table
mycursor = mydb.cursor()

sql = "INSERT INTO UploadLog (Uploader,MusicBrainzID,Source) VALUES (%s, %s)"
val = ("WEBFORM INPUT", "WEBFORM INPUT")
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

#call ffmpeg to produce the spectogram of audio files
import os

import subprocess
os.chdir('DIRECTORY')
subprocess.call(['for %%a in *.flac *.alac *.wav *.aac *.wma *.opus *.m4a *.ape do ffmpeg -i "%%a" -lavfi showspectrumpic=s=1920x1080 "%%~na.png"'])
