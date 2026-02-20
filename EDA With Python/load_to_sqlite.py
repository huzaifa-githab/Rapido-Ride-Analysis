import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_excel("Data/Cleaned/rides_cleaned.xlsx")

# Connect to SQLite DB
conn = sqlite3.connect("SQL/rapido.db")

# Save table
df.to_sql("rides", conn, if_exists="replace", index=False)

conn.close()

print("Database created and data loaded successfully.")
