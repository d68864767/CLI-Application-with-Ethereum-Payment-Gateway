```python
# database_setup.py

import psycopg2
from psycopg2 import sql
from config import DATABASE_CONFIG

# Establish a connection to the database
try:
    conn = psycopg2.connect(
        host=DATABASE_CONFIG['host'],
        port=DATABASE_CONFIG['port'],
        user=DATABASE_CONFIG['user'],
        password=DATABASE_CONFIG['password'],
        dbname=DATABASE_CONFIG['database']
    )
    print("Database connection successful")
except Exception as e:
    print(f"Failed to connect to the database: {e}")

# Create a cursor object
cur = conn.cursor()

# Create a table to store transaction records and user data
try:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            transaction_id VARCHAR(255) NOT NULL,
            amount DECIMAL(18, 8) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("Table 'transactions' created successfully")
except Exception as e:
    print(f"Failed to create table: {e}")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
```
