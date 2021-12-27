# DROP TABLES
artists_songs_length_by_session_drop = "drop table IF EXISTS artists_songs_length_by_session"
artists_songs_users_by_userId_session_drop = "drop table IF EXISTS artists_songs_users_by_userId_session"
users_per_song_drop = "drop table IF EXISTS users_per_song"

# CREATE KEYSPACE
create_keyspace = """
    CREATE KEYSPACE IF NOT EXISTS udacity 
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""

# CREATE TABLES
artists_songs_length_by_session_create = """CREATE TABLE IF NOT EXISTS artists_songs_length_by_session (sessionId int,
                    itemInSession int,
                    artist text,
                    song text,
                    length float,                    
                    PRIMARY KEY (sessionId, itemInsession))""" 
artists_songs_users_by_userId_session_create = """CREATE TABLE IF NOT EXISTS artists_songs_users_by_userId_session(userId int,
                    sessionId int,
                    itemInSession int,
                    artist text,
                    song text,
                    user text,    
                    PRIMARY KEY ((userId, sessionId),itemInSession))"""
users_per_song_create = """CREATE TABLE IF NOT EXISTS users_per_song(song text,
                    userId int,
                    user text,
                    PRIMARY KEY (song,userId))"""
# INSERT RECORDS
artists_songs_length_by_session_insert = "INSERT INTO artists_songs_length_by_session (sessionId,itemInSession,artist, song, length) VALUES (%s, %s, %s, %s, %s)"
artists_songs_users_by_userId_session_insert = "INSERT INTO artists_songs_users_by_userId_session (userId, sessionId,itemInSession, artist, song, user)  VALUES (%s, %s, %s, %s, %s, %s)"
users_per_song_insert = "INSERT INTO users_per_song (song, userId,user) VALUES (%s, %s,%s)"

# FIND RECORDS
artists_songs_length_by_session_select = "select artist,song,length from artists_songs_length_by_session WHERE sessionId = 338 and itemInSession = 4"
artists_songs_users_by_userId_session_select = "select artist,song,user from artists_songs_users_by_userId_session WHERE userId = 10 and sessionId = 182"
users_per_song_select = "select user from users_per_song WHERE song = 'All Hands Against His Own'"