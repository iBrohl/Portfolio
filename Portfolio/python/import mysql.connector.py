import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", passwd="2016b720", database="b720")


# def inserta_producto(Productos, Cantidad):
    #cur = cnn.cursor()
    # sql='''INSERT INTO inventario_rack (Productos, Cantidad)
    VALUES('Cables de Telefono', 4)'''.format(Productos, Cantidad)
    cur.execute(sql)
    n=cur.rowcount
    cnn.commit()
    cur.close()
    return n

print(inserta_producto('Cables de Telefono', 4))
