import sqlite3
import random

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table safely
cursor.execute('''
CREATE TABLE IF NOT EXISTS hospital (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    city TEXT,
    service TEXT,
    cost INTEGER,
    rating REAL,
    distance REAL
)
''')

# NCR Cities
cities = ['Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Ghaziabad']

# Services
services = ['surgery', 'cardiology', 'orthopedic', 'neurology', 'general']

# Hospital name prefixes
names = ['Apollo', 'Fortis', 'Max', 'Medanta', 'AIIMS', 'Columbia Asia', 'Paras']

# Generate 500 entries
data = []

for i in range(500):
    name = random.choice(names) + " Hospital " + str(i+1)
    city = random.choice(cities)
    service = random.choice(services)
    cost = random.randint(20000, 80000)
    rating = round(random.uniform(3.5, 5.0), 1)
    distance = round(random.uniform(1, 20), 1)

    data.append((name, city, service, cost, rating, distance))

# Insert data
cursor.executemany('''
INSERT INTO hospital (name, city, service, cost, rating, distance)
VALUES (?, ?, ?, ?, ?, ?)
''', data)

conn.commit()
conn.close()

print("500 hospital entries added successfully!")