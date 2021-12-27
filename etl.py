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
runQuery(session, artists_songs_length_by_session_create)
insertIntoArtistsSongsLengthBySession(session, artists_songs_length_by_session_insert)
## SELECT statement to verify the data was entered into the table
rows = runQueryRows(session,artists_songs_length_by_session_select)
for row in rows:
    print (row.artist, row.song, row.length)

## Query 2: name of artist, song (sorted by itemInSession) and user (first and last name)\
## for userid = 10, sessionid = 182
runQuery(session,artists_songs_users_by_userId_session_create )
insertIntoArtistsSongsUsersByUserIdSession(session,artists_songs_users_by_userId_session_insert)
## SELECT statement to verify the data was entered into the table
rows = runQueryRows(session, artists_songs_users_by_userId_session_select)    
for row in rows:
    print (row.artist, row.song, row.user)
    
##Query 3: Every user name (first and last) in the music app history who listened to the song 'All Hands Against His Own'
runQuery(session, users_per_song_create)
insertIntoUsersPerSong(session,users_per_song_insert)
## SELECT statement to verify the data was entered into the table
rows = runQueryRows(session, users_per_song_select)
for row in rows:
    print (row.user)

#DROP TABLES
runQuery(session, artists_songs_length_by_session_drop)
runQuery(session, artists_songs_users_by_userId_session_drop)
runQuery(session, users_per_song_drop)

#SHUTDOWN
session.shutdown()
cluster.shutdown()