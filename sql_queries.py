# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# I've added NOT NULL to most fields.
# However, in table songplays song_id and artist_id are exempt as the song_select query will not always find a match
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
(songplay_id serial, start_time varchar NOT NULL, user_id int NOT NULL, level varchar NOT NULL, song_id varchar, artist_id varchar, session_id varchar NOT NULL, location varchar NOT NULL, user_agent varchar NOT NULL, primary key (songplay_id))
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
(user_id varchar NOT NULL, first_name varchar NOT NULL, last_name varchar NOT NULL, gender varchar NOT NULL, level varchar NOT NULL, primary key(user_id))
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
(song_id varchar, title varchar NOT NULL, artist_id varchar NOT NULL, year int NOT NULL, duration numeric NOT NULL, primary key(song_id))
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
(artist_id varchar, name varchar NOT NULL, location varchar NOT NULL, latitude numeric, longitude numeric, primary key(artist_id))
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
(start_time varchar NOT NULL, hour int NOT NULL, day int NOT NULL, week int NOT NULL, month int NOT NULL, year int NOT NULL, weekday int NOT NULL, primary key(start_time))
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s)
""")

# if a user already exists then update the record from free to paid
user_table_insert = ("""
INSERT INTO users
(user_id, first_name, last_name, gender, level)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE set level=EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs
(song_id, title, artist_id, year, duration)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists
(artist_id, name, location, latitude, longitude)
VALUES
(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time
(start_time, hour, day, week, month, year, weekday)
VALUES
(%s,%s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS
song_select = ("""
SELECT songs.song_id, songs.artist_id FROM (songs
JOIN artists ON songs.artist_id = artists.artist_id)
WHERE songs.title = %s AND
artists.name = %s AND
songs.duration = %s
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]