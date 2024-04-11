import sqlite3
connection = sqlite3.connect('carbon_footprint.db')

cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS CarbonFootprint 
(id INTEGER PRIMARY KEY AUTOINCREMENT, Organization TEXT,  
EnergyUsage REAL, Waste REAL, Travel REAL) ''')

def insert_data(company, energyusage, waste, travel):
    insert_query = '''
        INSERT INTO CarbonFootprint(Organization, EnergyUsage, Waste, Travel)
        VALUES (?,?,?,?);'''
    data_input = (company, energyusage, waste, travel)
    cursor.execute(insert_query, data_input)
    cursor.execute("SELECT Organization, EnergyUsage, Waste, Travel FROM CarbonFootprint")
    #print(cursor.fetchall())
    connection.commit()
    connection.close()

