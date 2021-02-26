import pymysql
from decouple import config

class Db:
    """
    Class for control operation in data base 
    """
    cursor = None
    conn = None

    def __init__(self):
        self.conn = pymysql.connect(
            host=config('HOST'),
            user=config('USER'),
            password=config('PASSWORD'),
            db=config('DATA_BASE'))

        self.cursor = self.conn.cursor()

    def insert(self, temperature, humidity):
        """
        Insert in table
        """
        query =  "INSERT INTO data (temperature, humidity) VALUES ({}, '{}');".format(float(temperature), float(humidity))
        self.cursor.execute(query)
        self.save()

    def save(self):
        """
        Save changes in Database
        """
        self.conn.commit()

    def all(self):
        """
        Get all data in table
        """
        query = "SELECT * FROM data"
        self.cursor.execute(query)
        result = (self.cursor.fetchall())
        data = []
        for item in result:
            print(item)
            data.append(item)
        return data


database = Db()