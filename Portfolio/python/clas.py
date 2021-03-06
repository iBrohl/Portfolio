import mysql.connector

class Cities:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root",
        passwd="2016b720", database="bdEjemploPy")

    def __str__(self):
        datos=self.consulta_ciudades()
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux

    def consulta_ciudades ():
        cur = self.cnn.cursor ()
        cur.execute ("SELECT * FROM countries")
        datos = cur.fetchall ()
        cur.close ()
        return datos

    def inserta_ciudad (ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor ()
        sql='''INSERT INTO countries (ISO3, CountryName, Capital, CurrencyCode)
        VALUES ('{}', '{}', '{}', '{}'''.format (ISO3, CountryName, Capital, CurrencyCode)
        cur.execute (sql)
        n=cur.rowcount
        self.cnn.commit ()
        cur.close ()
        return n

    def elimina_ciudad (Id):
        cur = self.cnn.cursor ()
        sql='''DELETE FROM Countries WHERE Id = ()'''.format (Id)
        cur.execute (sql)
        n=cur.rowcount
        self.cnn.commit ()
        cur.close ()
        return n

    def modifica_ciudad(Id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor() 
        sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}', CurrencyCode='{}' WHERE Id={}'''.format(ISO3, CountryName, Capital, CurrencyCode, Id)
        cur.execute(sql)
        n=cur.rowcount 
        self.cnn.commit()
        cur.close()
        return n