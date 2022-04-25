import mysql-connector

cnn = mysql.connector.connect(host="localhost", user="root", passw="2016b720", database="world")
print(cnn)