import json
import psycopg2
from pathlib import Path

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="P@ssw0rd", port="5432")

cur = conn.cursor()




conn.commit()

cur.close()
conn.close()

