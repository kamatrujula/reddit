import pandas as pd
import json
import datetime
import psycopg2

df = pd.read_json('data.json')
#print("Hello World")

connection = psycopg2.connect(host="localhost",
                        port="write your post",
                        user="write your username",
                        password="write your password",
                        dbname="write your dbname",
                        sslmode='prefer')

cursor = connection.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS reddit_posts (
    Id INT PRIMARY KEY,
    Title VARCHAR(255),
    Score INT,
    Content TEXT,
    NumberOfComments INT,
    PublishDate TIMESTAMP,
    Link VARCHAR(255)
);
'''
cursor.execute(create_table)

def insert_data(cursor, df):
    # Insert data using DataFrame
    for index, row in df.iterrows():
        insert_query = '''
        INSERT INTO reddit_posts (Id, Title, Score, Content, NumberOfComments, PublishDate, Link)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (Id) DO UPDATE SET
        Title = EXCLUDED.Title,
        Score = EXCLUDED.Score,
        Content = EXCLUDED.Content,
        NumberOfComments = EXCLUDED.NumberOfComments,
        PublishDate = EXCLUDED.PublishDate,
        Link = EXCLUDED.Link;;
        '''
        cursor.execute(insert_query, (row['Id'], row['Title'], row['Score'], row['Content'], row['NumberOfComments'], row['PublishDate'], row['Link']))


insert_data(cursor, df)

connection.commit()
cursor.close()
connection.close()

print("Script executed")
