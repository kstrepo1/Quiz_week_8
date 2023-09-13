import matplotlib.pyplot as plt
import sqlite3 as sq

connection = sq.connect('climate.db')

print(connection.total_changes)

sql_query = """SELECT * FROM climateData;"""
cursor = connection.cursor()
cursor.execute(sql_query)

result = cursor.fetchall()

years = []
co2 = []
temp = []

for a in result:
    years.append(a[0])
    co2.append(a[1])
    temp.append(a[2])

if connection:
    connection.close()
    print("The SQL connection is closed")


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
