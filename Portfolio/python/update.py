import mysql.connector

cnn = mysql.connector.connect (host="localhost", user="root", passwd="2016b720", database="bdejemplopy")



def modifica_ciudad(Id, ISO3, CountryName, Capital, CurrencyCode):
    cur = cnn.cursor() 
    sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}', CurrencyCode='{}' WHERE Id={}'''.format(ISO3, CountryName, Capital, CurrencyCode, Id)
    cur.execute(sql)
    n=cur.rowcount 
    cnn.commit()
    cur.close()
    return n

print( modifica_ciudad(9, 'EUA', 'Estados Unidos', 'New York', 'DLS')  )