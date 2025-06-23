import mysql.connector

conn=mysql.connector.connect(
    host='localhost',user='root',password='root',database='upi'
)
print(conn.is_connected())
cursor=conn.cursor()

cursor.execute("call user('vamsi@gmail.com')")

print(cursor.fetchall())
cursor.close()
conn.close()