import mysql.connector
import dbconfig as cfg

class PlanetDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    # Add planet to database table.
    def create(self, values):
        cursor = self.getcursor()
        sql="insert into planets (name, size, moons, distance) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    # Get all data from planets table.
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from planets"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    # Find planet by id.
    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from planets where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    # Update planet in database table.
    def update(self, values):
        cursor = self.getcursor()
        sql="update planets set name=%s, size=%s, moons=%s, distance=%s where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    # Delete planet from database table.  
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from planets where id=%s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','name','size', "moons", "distance"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
planetsDAO = PlanetDAO()