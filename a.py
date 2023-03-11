import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="")
c = mydb.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS monthly_reports")