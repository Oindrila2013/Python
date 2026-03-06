import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data succesfully')

import pandas as pd
tables =  pd.read_sql("""SELECT * 
                      FROM sqlite_master
                      WHERE type='tables';""", conn)
print(tables)

teams = pd.read_sql("""SELECT * 
                    FROM Teams;""", conn)
print(teams)

matches = pd.read_sql("""SELECT * 
                    FROM Match;""", conn)
print(matches)

MI_wins = pd.read_sql("""SELECT * 
                      FROM Match
                      WHERE MATCH_WINNER == 7;""", conn)
print(MI_wins)

MI_S8_S9 = pd.read_sql("""SELECT * 
                       FROM Match
                       WHERE Match_WINNER == 7 AND SEASON ID IN (8,9);""", conn)
print(MI_S8_S9)

new_teams = pd.read_sql("""SELECT * 
                       FROM Team
                       WHERE Team_NAME LIKE 'De%');""", conn)
print(new_teams)

min_max_mirgin = pd.read_sql("""SELECT MIN(WIN_MARGIN), MAX(WIN_MARGIN)
                            FROM Match;""", conn)
print(min_max_mirgin)