import psycopg2
import json
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="P@ssw0rd", port="5432")

cur = conn.cursor()
with open('output.json',  encoding="utf8") as file:
    data = json.load(file)


cur.execute("""CREATE TABLE IF NOT EXISTS event (
    id SERIAL PRIMARY KEY,
    title text,
    location text,
    date_time text,
    artist text[],
    works text[],
    image_link text
) ;
""")

conn.commit()

query_sql = ''' INSERT INTO event (title,location,date_time,artist,works,image_link)
VALUES (
    %(title)s,
    %(location)s,
    %(date_time)s,
    %(artist)s,
    %(works)s,
    %(image_link)s
);
'''
for line in data:
    cur.execute(query_sql,line)

conn.commit()

cur.close()
conn.close()
