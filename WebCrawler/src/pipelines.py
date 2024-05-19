# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class srcPipeline:
    def __init__(self):
        self.conn = psycopg2.connect(host="pythonproject-postgres-1", dbname="postgres", user="postgres", password="1234", port="5432")
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS event (
            id SERIAL PRIMARY KEY,
            title text,
            location text,
            date_time text,
            artist text[],
            works text[],
            image_link text
        ) ;
        """)
        self.conn.commit()
    def process_item(self, item, spider):
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
        self.cur.execute(query_sql, item)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()