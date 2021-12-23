# DROP TABLES
music_library_drop = "drop table IF EXISTS music_library"
music_library_1_drop = "drop table IF EXISTS music_library1"
music_library_2_drop = "drop table IF EXISTS music_library2"

# CREATE TABLES
music_library_create = """CREATE TABLE IF NOT EXISTS music_library (artist text,
                    song text,
                    length float,
                    itemInSession int,
                    sessionId int,
                    PRIMARY KEY (sessionId, itemInsession))""" 
music_library_1_create = """CREATE TABLE IF NOT EXISTS music_library1(artist text,
                    song text,
                    user text,
                    itemInSession int,
                    userId int,
                    sessionId int,
                    PRIMARY KEY ((userId, sessionId),itemInSession))"""
music_library_2_create = """CREATE TABLE IF NOT EXISTS music_library2(song text,
                    user text,
                    PRIMARY KEY (song))"""
# INSERT RECORDS
music_library_insert = "INSERT INTO music_library (artist, song, length, itemInSession, sessionId) VALUES (%s, %s, %s, %s, %s)"
music_library_1_insert = "INSERT INTO music_library1 (artist, song, user, itemInSession, userId, sessionId)  VALUES (%s, %s, %s, %s, %s, %s)"
music_library_2_insert = "INSERT INTO music_library2 (song, user) VALUES (%s, %s)"

# FIND RECORDS
music_library_select = "select * from music_library WHERE sessionId = 338 and itemInSession = 4"
music_library_1_select = "select * from music_library1 WHERE userId = 10 and sessionId = 182"
music_library_2_select = "select * from music_library2 WHERE song = 'All Hands Against His Own'"