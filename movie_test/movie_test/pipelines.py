import pymysql
class MoviePipeline:
    def __init__(self, db_config):
        self.db_config = db_config
    @classmethod
    def from_crawler(cls, crawler):
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Cc2002',
            'database': 'douban_test',
            'charset': 'utf8mb4'
        }
        return cls(db_config)
    def open_spider(self, spider):
        self.conn = pymysql.connect(**self.db_config)
        self.cur = self.conn.cursor()
        self.init_db()
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
    def init_db(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS movie250 (
                id INT PRIMARY KEY AUTO_INCREMENT,
                info_link TEXT,
                pic_link TEXT,
                cname VARCHAR(255),
                ename VARCHAR(255),
                score NUMERIC,
                rated NUMERIC,
                instroduction TEXT,
                info TEXT
            )
        '''
        self.cur.execute(sql)
        self.conn.commit()
    def process_item(self, item, spider):
        sql = '''
            INSERT INTO movie250 (
                info_link, pic_link, cname, ename, score, rated, instroduction, info
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        self.cur.execute(sql, (
            item['info_link'], item['pic_link'], item['cname'], item['ename'],
            item['score'], item['rated'], item['instroduction'], item['info']
        ))
        self.conn.commit()
        return item
