# Import Python packages 
import cassandra
from cassandra.cluster import Cluster
from functions import *
from sql_queries import *

convertDataToCsv()


# Make a connection to a Cassandra instance in your local machine 
# (127.0.0.1)
try: 
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
except Exception as e:
    print(e)

#creates keyspace    
runQuery(session,create_keyspace)

#Set KEYSPACE
try:
    session.set_keyspace('udacity')
except Exception as e:
    print(e)

    
##Query 1:  artist, song title and song's length in the music app history that was heard during \
## sessionId = 338, and itemInSession = 4
runQuery(session, music_library_create)
insertIntoMusicLibrary(session, music_library_insert)
## SELECT statement to verify the data was entered into the table
rows = runQueryRows(session,music_library_select)
for row in rows:
    print (row.artist, row.song, row.length)

## Query 2: name of artist, song (sorted by itemInSession) and user (first and last name)\
## for userid = 10, sessionid = 182
runQuery(session,music_library_1_create )
insertIntoMusicLibrary1(session,music_library_1_insert)
## SELECT statement to verify the data was entered into the table
rows = runQueryRows(session, music_library_1_select)    
for row in rows:
    print (row.artist, row.song, row.user)
    
##Query 3: Every user name (first and last) in the music app history who listened to the song 'All Hands Against His Own'
runQuery(session, music_library_2_create)
insertIntoMusicLibrary2(session,music_library_2_insert)
## SELECT statement to verify the data was entered into the table
rows = runQueryRows(session, music_library_2_select)
for row in rows:
    print (row.user)

#DROP TABLES
runQuery(session, music_library_drop)
runQuery(session, music_library_1_drop)
runQuery(session, music_library_2_drop)

#SHUTDOWN
session.shutdown()
cluster.shutdown()