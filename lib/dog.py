import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    all =[]
    def __init__(self, name, breed):
        self.id = None
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS dogs(
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT
            ) '''
        CURSOR.execute(sql) 
    
    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS dogs
            '''
        CURSOR.execute(sql)
        

    def save(self):
        sql = '''
            INSERT INTO dogs(name, breed)
            VALUE(?, ?)'''
        CURSOR.execute(sql, (self.name, self.breed))
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, breed):
        dog = cls(name, breed)
        dog.save()
        return dog
    
    
    def new_from_db(cls, row):
        return cls(row[0], row[1], row[2])
    
    @ classmethod
    def get_all(cls):
        sql = '''
            SELECT * 
            FROM dogs
            '''
        all = CURSOR.execute(sql).fetchall()
        cls.all = [cls.new_from_db(row) for row in all]

    @classmethod
    def find_by_name(cls,name):
        sql = '''
        SELECT * 
        FROM dogs 
        WHERE name = ?
        LIMIT 1 
        '''
        dogs = CURSOR.execute(sql, (name,)).fetchone()
        return cls.new_from_db(dogs)
    
    @classmethod
    def find_by_name(cls,id):
        sql = '''
        SELECT * 
        FROM dogs 
        WHERE id = ?
        LIMIT 1 
        '''
        dogs = CURSOR.execute(sql, (id,)).fetchone()
        return cls.new_from_db(dogs)

