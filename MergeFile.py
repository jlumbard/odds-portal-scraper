import pandas
df = pandas.read_csv('mlb_elo.csv')
import sqlite3
conn = sqlite3.connect('oddsportal.db')
df2 = pandas.read_sql_query("select * from matches",conn)
result = pandas.concat([df,df2],axis=1,sort=False)
result.to_csv('unjoinedmerge.csv')
