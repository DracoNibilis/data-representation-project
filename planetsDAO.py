import mysql.connector

class PlanetDAO:
    host = ""
    user = ""
    password = ""
    database = ""

    connection = ""
    cursor = ""

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "datarepresentation"

    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self,values):
        cursor = self.getCursor()
        sql = "insert into planets (planet, size, moons, distance) values (%s,%s,%s,%s)"
        cursor.execute(sql,values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from planets"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result

    def findById(self,id):
        cursor = self.getCursor()
        sql = "select * from planets where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result

    def update(self,values):
        cursor = self.getCursor()
        sql = "update planets set planet=%s, size=%s, moons=%s, distance=%s where id = %s"
        cursor.execute(sql,values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getCursor()
        sql = "delete from planets where id=%s"
        values = (id,)

        cursor.execute(sql,values)

        self.connection.commit()
        self.closeAll()

planetDAO = PlanetDAO()


