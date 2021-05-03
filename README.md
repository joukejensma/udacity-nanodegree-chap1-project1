## (Nontechnical) Project summary:
The objective is to create a database where analyses can be performed upon for the Sparkify company. We combine listening data from songs from users with access logs into a central table which ties user listening info to songs.

## File overview:
- create_tables.py
Run this one in the terminal to refresh the database. Tables will be dropped and recreated if required.
- sql_queries.py 
Overview of all CREATE and INSERT queries required to perform this project.
- etl.ipynb
Easy demo to read in a bit of data and test the queries before creating etl.py, where all available data is processed.
- etl.py
Ingest all available log and song data and insert into the database.
- test.ipynb 
Testing Jupyter notebook to examine if all queries work as expected.
Final result is that one entry has songId NOT NULL which apparently is OK.

## Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
It's clear that the songplays is supposed to be the table where analyses can be done upon as it contains all relevant information that might be required in an analysis (it ties user listening info to songs). 

##     State and justify your database schema design and ETL pipeline.
The songplay table is the fact table where analysis can be done upon. The remaining tables are dimension tables.
I've chosen the songplay_id to be auto generated (serial type) as it is tied to a single event where a particular user listens to a particular song.
All other columns can be filled from the available data.
I had some doubts as how to store the datetime column in the time table, but chose to keep it as a timestamp.
A possibility could be to store it as a TIMESTAMP type. However, we haven't covered that in the lectures so at this point I'm not sure if I was supposed to do that.
The id columns I've chosen to have constraint UNIQUE (users, songs, artists tables). When doing this I had to add the ON CONFLICT tag as there might be duplicates in the input data. For now I've assumed that users, songs and artists id's are unique as well in the input data so on a conflict I've decided to do nothing with the record.

## etl.py specifics
When writing etl.py I could copy snippets from the notebook file. I had to iterate over records though, so that's an addition.

## [Optional] Provide example queries and results for song play analysis.
I've skipped this part.

